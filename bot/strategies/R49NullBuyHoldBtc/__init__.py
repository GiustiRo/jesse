from jesse.strategies import Strategy
from jesse import utils

# Fracción del balance usada como nocional: deja margen para el fee de entrada
# y para que la posición quede en ~1x sin rozar el límite de margen aislado.
NOTIONAL_FRACTION = 0.99


class R49NullBuyHoldBtc(Strategy):
    """
    r49 Fase 0, benchmark nulo (i): buy & hold BTC.
    Una única entrada larga ~1x en la primera vela y nunca sale; el motor cierra
    la posición al final de la ventana. Sin stops, sin rebalanceo. Paga funding.
    """

    def should_long(self) -> bool:
        return not self.vars.get('entered', False)

    def should_short(self) -> bool:
        return False

    def should_cancel_entry(self) -> bool:
        return False

    def go_long(self) -> None:
        qty = utils.size_to_qty(self.balance * NOTIONAL_FRACTION, self.price, fee_rate=self.fee_rate)
        self.buy = qty, self.price

    def go_short(self) -> None:
        pass

    def on_open_position(self, order) -> None:
        self.vars['entered'] = True

    def update_position(self) -> None:
        pass
