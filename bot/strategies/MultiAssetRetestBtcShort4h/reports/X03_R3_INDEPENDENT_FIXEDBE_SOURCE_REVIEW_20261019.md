# X03 R3 — revisión independiente de fuente fixedBE

Se leyeron por MCP las fuentes completas PortComparePaxgMarket4h y X03ExecPaxgFixedBeR301, y X03_R3_FIXEDBE_SOURCE_QA_20261019.md. No se ejecutó otro job de QA ni backtest desde este rol.

La transformación textual completa coincide exactamente con los tres cambios permitidos:

1. Renombrar la clase a X03ExecPaxgFixedBeR301.
2. Añadir BE_FEE_ANCHOR = 0.00045 con dos comentarios de origen y alcance.
3. Sustituir self.fee_rate por BE_FEE_ANCHOR únicamente en el piso stop = max(stop, entry * (1 + 2.5 * ...)).

No hay diferencias adicionales de bytes. La fuente original coincide con la versión PAXG preservada en R2. Las lecturas de self.fee_rate pasan de cinco a cuatro por la sustitución del único término; las restantes permanecen exactas. La constante aparece una vez definida y una vez usada. No se sobrescribe fee_rate.

Por identidad de todo el resto de la fuente se conservan HP, best_r/be_r, ATR/trailing, tightening a 5R/8R, guardas de stop, entradas MARKET y fresh quote M1, horarios, sizing, riesgo compartido, reservas, lot rounding, callbacks y logs. El clon se usa sólo para PAXG; BTC y SPY no se cambian.

La QA reportada en job 55146e3217cc48ddb080d4186dcc11d1 succeeded contiene 59 checks. Revisé el código de ese harness y su cobertura: AST de métodos/constantes, intervención única, nominal/fee alto, trigger y pretrigger, no aflojar stop, guarda frente a precio, trailing dominante, ATR inválido, timeout heredado y ejemplo de fee neto. No repetí esos tests; la verificación independiente de este rol es la lectura y la transformación textual exacta.

La QA es sintética con ATR controlado: no verifica cobro real del motor, matching histórico ni paridad de recorridos. El propio reporte lo declara. Las cuatro paridades nominales económicas siguen siendo obligatorias antes del stress. Precios, timestamps, cantidades, fees y PNL deben coincidir con cada referencia; nombre de clase y logs no son economía.

El ancla no garantiza BE neto bajo .00070. En el ejemplo de entrada 2661, el piso fijo 2663.993625 produce pérdida neta por unidad de aproximadamente −0.73387054 tras fee alto, antes de otros costes. Trailing y guardas pueden dominar el piso. El contraste al mismo fee estima el efecto total de la política en este simulador, incluyendo capital y ocupación posteriores; no un efecto puro de comisión ni alpha BTC.

Sin objeciones materiales de fuente o QA. Aprobación de implementación condicionada a paridad nominal y auditorías económicas/calendario. No se selecciona política por beneficio, no hay promoción ni apertura de 2026.
