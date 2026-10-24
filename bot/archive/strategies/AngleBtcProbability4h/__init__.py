import math
from collections import deque
from datetime import datetime, timezone

import numpy as np
import jesse.indicators as ta
from jesse.strategies import Strategy

BAR_MS = 4 * 60 * 60 * 1000
MINUTE_MS = 60 * 1000
LEARNING_WINDOW = 1080  # 180 days of non-overlapping four-hour outcomes.
MIN_STATE_CASES = 80  # Avoid decisions supported by a handful of pattern matches.
PRIOR_CASES = 20.0  # Balanced zero-mean, unit-R-second-moment shrinkage prior.
BASE_FEE = 0.00045
FRICTION_BUFFER = 0.001  # Forecast haircut and sizing reserve, NOT simulated slippage.
TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
STOP_LEVERAGE_BUFFER = 0.75  # Keep25%inside ideal1/leverage; not exact liquidation math.


class AngleBtcProbability4h(Strategy):
    """Causal four-state monetary expectancy with explicit abstention.

    Two return signs define four states. No trend/reversal direction is assumed.
    Smoothed win probability is diagnostic; net payoff and uncertainty gate trades.
    This is a research hypothesis, not a claim of calibrated probabilities.
    """

    def _model(self):
        if 'probability_model' not in self.vars:
            self.vars['probability_model'] = {
                'observations': deque(),
                'count': np.zeros(4, dtype=np.int64),
                'sum': np.zeros((4, 2)),
                'sum_square': np.zeros((4, 2)),
                'wins': np.zeros((4, 2), dtype=np.int64),
                'pending': None,
                'last_processed': None,
                'labels_total': 0,
                'missing_labels': 0,
                'year': None,
                'skip_window': 0, 'skip_state_cases': 0, 'skip_edge': 0,
                'skip_stop_safety': 0, 'skip_qty': 0,
                'long_signals': 0, 'short_signals': 0,
            }
        return self.vars['probability_model']

    def _log_model_summary(self, label):
        m = self._model()
        self.log('ANGLE_PROBABILITY_SUMMARY ' + label + ' cumulative '
                 + str({k: (len(m['observations']) if k == 'window_length' else
                            m['count'].tolist() if k == 'state_counts' else m[k])
                        for k in ('labels_total', 'missing_labels', 'window_length',
                                  'state_counts', 'skip_window', 'skip_state_cases',
                                  'skip_edge', 'skip_stop_safety', 'skip_qty',
                                  'long_signals', 'short_signals')}))

    def _label(self, pending):
        # Only source minutes after the previous decision and already CLOSED now
        # can mature its label. No forward-fill or stale multi-hour substitute.
        if int(self.time) != pending['time'] + BAR_MS:
            return None
        minutes = self.get_candles(self.exchange, self.symbol, '1m')
        if len(minutes) < 240:
            return None
        minutes = minutes[-240:]
        expected = pending['time'] + np.arange(240, dtype=np.int64) * MINUTE_MS
        assert np.all(minutes[:, 0] < self.time), 'PROBABILITY_FUTURE_MINUTE'
        if not np.array_equal(minutes[:, 0].astype(np.int64), expected):
            return None
        if not np.isfinite(minutes[:, :5]).all() or np.any(minutes[:, 1:5] <= 0):
            return None
        entry = pending['entry']
        distance = pending['distance']
        outcomes = []
        for side in (1, -1):
            stop = entry - side * distance
            exit_price = float(minutes[-1, 2])
            for row in minutes:
                opening = float(row[1])
                # A protective STOP crossed by an opening gap fills at that
                # adverse minute opening; otherwise its first touched stop wins.
                if (side == 1 and opening <= stop) or (side == -1 and opening >= stop):
                    exit_price = opening
                    break
                if (side == 1 and row[4] <= stop) or (side == -1 and row[3] >= stop):
                    exit_price = stop
                    break
            # Signal costs remain fixed in later effective-fee stress. Every
            # virtual outcome bears both taker fees plus a conservative haircut.
            cash_per_unit = (side * (exit_price - entry)
                             - BASE_FEE * (entry + exit_price)
                             - FRICTION_BUFFER * entry)
            outcomes.append(cash_per_unit / distance)
        return np.asarray(outcomes)

    def _record(self, pending, outcomes):
        model = self._model()
        observations = model['observations']
        if len(observations) == LEARNING_WINDOW:
            state, old = observations.popleft()
            model['count'][state] -= 1
            model['sum'][state] -= old
            model['sum_square'][state] -= old * old
            model['wins'][state] -= (old > 0).astype(np.int64)
        state = pending['state']
        observations.append((state, outcomes.copy()))
        model['count'][state] += 1
        model['sum'][state] += outcomes
        model['sum_square'][state] += outcomes * outcomes
        model['wins'][state] += (outcomes > 0).astype(np.int64)
        model['labels_total'] += 1
        assert int(model['count'].sum()) == len(observations)
        assert np.all(model['count'] >= 0)

    def before(self):
        assert self.symbol == 'BTC-USDT' and self.timeframe == '4h'
        assert self.is_futures_trading
        model = self._model()
        if model['last_processed'] == int(self.time):
            return
        model['last_processed'] = int(self.time)
        year = datetime.fromtimestamp(self.time / 1000, timezone.utc).year
        if model['year'] is not None and year != model['year']:
            self._log_model_summary('through_year_' + str(model['year']))
        model['year'] = year
        pending = model['pending']
        if pending is not None:
            outcomes = self._label(pending)
            if outcomes is None:
                model['missing_labels'] += 1
                # Eight failed maturation attempts with zero valid labels is a
                # data/cadence failure, not evidence that the economic gate abstains.
                # Occasional gaps after valid observations remain permitted.
                if model['labels_total'] == 0 and model['missing_labels'] >= 8:
                    self._log_model_summary('invalid_m1_coverage')
                    raise AssertionError('ANGLE_NO_MATURED_LABELS: verify240closed_contiguous_M1_and_clock')
            else:
                self._record(pending, outcomes)
        c = self.candles
        model['pending'] = None
        if len(c) < 30:
            return
        # All three closes are known now. Equal closes join the non-positive
        # state; there is no extra flat-return threshold to fit.
        closes = c[-3:, 2]
        if not np.isfinite(closes).all() or np.any(closes <= 0):
            return
        state = 2 * int(closes[1] > closes[0]) + int(closes[2] > closes[1])
        atr = float(ta.atr(c))
        distance = 3 * atr  # Emergency stop, not an optimized entry filter.
        if not (math.isfinite(distance) and 0 < distance < float(self.price)):
            return
        # Ideal liquidation distance1/L ignores maintenance/fees. Staying25%
        # inside it avoids obviously unprotected labels, without promising an
        # exact exchange liquidation boundary. This is not an optimizable gate.
        if distance / float(self.price) > STOP_LEVERAGE_BUFFER / self.leverage:
            model['skip_stop_safety'] += 1
            return
        model['pending'] = {'state': state, 'entry': float(self.price),
                            'distance': distance, 'time': int(self.time)}

    def _decision(self):
        if self.vars.get('decision_time') == int(self.time):
            return self.vars['decision_side']
        self.vars['decision_time'] = int(self.time)
        self.vars['decision_side'] = 0
        model = self._model()
        current = model['pending']
        # Runtime startup is fully retained as cash in the backtest. Warm-up
        # candles supply ATR only; no future/pretrained outcome table is loaded.
        if current is None or len(model['observations']) < LEARNING_WINDOW:
            model['skip_window'] += 1
            return 0
        state = current['state']
        n = int(model['count'][state])
        if n < MIN_STATE_CASES:
            model['skip_state_cases'] += 1
            return 0
        total = n + PRIOR_CASES
        mean = model['sum'][state] / total
        variance = np.maximum((model['sum_square'][state] + PRIOR_CASES) / total
                              - mean * mean, 0.0)
        standard_error = np.sqrt(variance / total)
        # This one-SE lower score is a conservative decision heuristic, NOT a
        # confidence statement under independent observations or a p-value.
        lower = mean - standard_error
        direction = int(np.argmax(lower))
        if not np.isfinite(lower).all() or lower[direction] <= 0:
            model['skip_edge'] += 1
            return 0
        side = 1 if direction == 0 else -1
        entry = current['entry']
        distance = current['distance']
        if distance / entry > STOP_LEVERAGE_BUFFER / self.leverage:
            model['skip_stop_safety'] += 1
            return 0
        stop = entry - side * distance
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        # The single BTC route starts at1%, below the approved3%/8% ceilings.
        unit_risk = distance + self.fee_rate * (entry + stop) + FRICTION_BUFFER * entry
        qty = min(capital * TRADE_RISK / unit_risk,
                  capital * NOTIONAL_CAP / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision only; native lot/min-notional must precede live use.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            model['skip_qty'] += 1
            return 0
        assert qty * unit_risk <= capital * TRADE_RISK + 1e-8
        self.vars['plan'] = {
            'qty': qty, 'distance': distance, 'entry': entry, 'state': state,
            'state_cases': n, 'expected_net_r': float(mean[direction]),
            'one_se_lower_r': float(lower[direction]),
            'win_probability': float((model['wins'][state, direction] + PRIOR_CASES / 2) / total),
        }
        model['long_signals' if side == 1 else 'short_signals'] += 1
        self.vars['decision_side'] = side
        return side

    def should_long(self):
        return self._decision() == 1

    def should_short(self):
        return self._decision() == -1

    def go_long(self):
        p = self.vars['plan']
        self.buy = p['qty'], self.price

    def go_short(self):
        p = self.vars['plan']
        self.sell = p['qty'], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        p = self.vars['plan']
        self.vars['opened_time'] = int(self.time)
        entry = float(self.position.entry_price)
        distance = p['distance']
        assert distance / entry <= STOP_LEVERAGE_BUFFER / self.leverage + 1e-12, 'ANGLE_FILL_STOP_BEYOND_SAFETY'
        if self.is_long:
            self.stop_loss = abs(self.position.qty), entry - distance
        else:
            self.stop_loss = abs(self.position.qty), entry + distance

    def update_position(self):
        # If an emergency stop did not already close it intrabar, close at the
        # first next four-hour decision. Jesse does not reopen in that callback.
        if self.time - self.vars['opened_time'] >= BAR_MS:
            self.liquidate()

    def on_increased_position(self, order):
        raise AssertionError('PROBABILITY_PYRAMIDING_UNSUPPORTED')

    def on_reduced_position(self, order):
        raise AssertionError('PROBABILITY_PARTIAL_EXIT_UNSUPPORTED')

    def before_terminate(self):
        self._log_model_summary('final')
