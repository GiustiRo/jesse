import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

# r51 F1: copia literal en Jesse de la manga R2 (Core4h) de C6, tal como la define el arnés
# congelado `r50_f1b.r2_r3_decider(bars, retest=False)` (commit 5caf4a53). Sirve solo para
# confirmar que el arnés y Jesse coinciden; no es una variante nueva y no suma a N.
RETEST = False
# 1% del equity de la manga en riesgo hasta el stop inicial, con fees de ida y vuelta.
RISK_PER_TRADE = 0.01
# Techo de nocional sobre equity, igual que el arnés.
MAX_X = 2.0
# Stop inicial: 2·ATR14, con piso 0,8% y techo 5,5% del precio (calibración Core4h en BTC 4h).
STOP_ATR = 2.0
MIN_STOP_FRAC = 0.008
MAX_STOP_FRAC = 0.055
# Chandelier K1001/Core4h: mejor cierre − 4,2·ATR, endurecido ×0,78 desde 5R y ×0,62 desde 8R.
TRAIL_MULT = 4.2
# Break-even: R2 mide el progreso en R con el máximo extremo y lo activa en 1,75R; R3 con el
# mejor cierre y en 2,25R. El stop BE cubre 2,5 fees.
BE_R = 2.25 if RETEST else 1.75
BE_FEES = 2.5


class R51C6R2(Strategy):
    """C6/R2: ruptura del máximo de 26 velas de 4h con tendencia EMA20>EMA80 creciente,
    ADX≥26, RSI 52–76 y vela no extendida; entrada a mercado al cierre."""

    def before(self) -> None:
        c = self.candles
        e80 = ta.ema(c, period=80, sequential=True)
        self.vars['ind'] = dict(
            e20=float(ta.ema(c, period=20, sequential=True)[-1]),
            e80=float(e80[-1]), e80_4=float(e80[-5]),
            atr=float(ta.atr(c, period=14, sequential=True)[-1]),
            adx=float(ta.adx(c, period=14, sequential=True)[-1]),
            rsi=float(ta.rsi(c, period=14, sequential=True)[-1]),
            # Máximo de las 26 velas previas, sin la actual.
            hh26=float(c[-27:-1, 3].max()),
            h=float(c[-1, 3]), l=float(c[-1, 4]), c=float(c[-1, 2]),
        )

    def _setup(self) -> bool:
        d = self.vars['ind']
        vals = [d['e20'], d['e80'], d['e80_4'], d['atr'], d['adx'], d['rsi'], d['hh26']]
        return (bool(np.isfinite(vals).all()) and d['atr'] > 0 and d['c'] > d['e80']
                and d['e20'] > d['e80'] > d['e80_4'] and d['adx'] >= 26
                and 52 <= d['rsi'] <= 76 and d['h'] - d['l'] <= 3 * d['atr'])

    def _risk_qty(self, price: float, dist: float) -> float:
        eq = self.balance
        q = eq * RISK_PER_TRADE / (dist + 2 * self.fee_rate * price)
        return max(min(q, eq * MAX_X / price), 0.0)

    def should_long(self) -> bool:
        # El arnés no vuelve a entrar en la vela en que se cerró una posición.
        if self.vars.get('closed_idx') == self.index or not self._setup():
            return False
        d = self.vars['ind']
        if RETEST:
            entry = d['hh26']
            if entry < d['c'] <= entry + d['atr'] and 0 < 2 * d['atr'] < entry:
                dist = STOP_ATR * d['atr']
                self.vars['plan'] = dict(price=entry, dist=dist, qty=self._risk_qty(entry, dist), hi=entry)
                return self.vars['plan']['qty'] > 0
            return False
        if d['c'] > d['hh26']:
            frac = max(STOP_ATR * d['atr'] / d['c'], MIN_STOP_FRAC)
            if frac <= MAX_STOP_FRAC:
                dist = frac * d['c']
                self.vars['plan'] = dict(price=d['c'], dist=dist, qty=self._risk_qty(d['c'], dist), hi=d['h'])
                return self.vars['plan']['qty'] > 0
        return False

    def should_short(self) -> bool:
        return False

    def go_long(self) -> None:
        p = self.vars['plan']
        self.buy = p['qty'], (p['price'] if RETEST else self.price)

    def go_short(self) -> None:
        pass

    def should_cancel_entry(self) -> bool:
        # La orden límite de R3 vale una sola vela.
        return True

    def on_open_position(self, order) -> None:
        p = self.vars['plan']
        entry = p['price']
        self.vars['st'] = dict(entry=entry, r=p['dist'], stop=entry - p['dist'], best_close=entry,
                               extreme=p['hi'])
        self.vars['open_idx'] = self.index
        self.stop_loss = self.position.qty, entry - p['dist']

    def on_close_position(self, order, closed_trade) -> None:
        self.vars['closed_idx'] = self.index

    def update_position(self) -> None:
        # R3 se llena dentro de una vela; el arnés no mueve el trailing en esa vela.
        if not self.is_open or self.vars.get('open_idx') == self.index:
            return
        d, st = self.vars['ind'], self.vars['st']
        st['best_close'] = max(st['best_close'], d['c'])
        st['extreme'] = max(st['extreme'], d['h'])
        ref = st['best_close'] if RETEST else st['extreme']
        best_r = (ref - st['entry']) / st['r'] if st['r'] > 0 else 0.0
        mult = TRAIL_MULT * (0.62 if best_r >= 8 else (0.78 if best_r >= 5 else 1.0))
        new = st['best_close'] - mult * d['atr']
        if best_r >= BE_R:
            new = max(new, st['entry'] * (1 + BE_FEES * self.fee_rate))
        if st['stop'] < new < d['c']:
            st['stop'] = new
            self.stop_loss = self.position.qty, new
