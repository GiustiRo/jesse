# BTC fast mean reversion — receta descartada
Dashboard: http://localhost:9200/#/backtest/df044178-559e-4d34-848f-820825479701
## Configuración y solapamiento
BTC-only4h, long MARKET, régimen EMA200 ascendente6intervalos, RSI2<=10 yprecio<SMA5, salida media5dinámica/48helapsed, stop2.5ATR desde fillreal. Un único recipe; comparte premisa MR con sleeves anteriores, no edge independiente. Riesgo1%,10k/5xaislado/fee0.00045porlado,2020-10-15→2025-12-31exclusivo,2026reservado. Protocolo previo y fuente conservados.
## Resultado
258trades,WR67.829%,mediawin23.8241USDT/medialoss51.1017USDT,net−72.2266USDT,CAGR−0.13894%,DD−5.21323%,Sharpe−0.028764,0posicionesterminales.
PNLantesdefees+519.9777;fees592.2043 consumenlaventajabruta. El altoacierto no creaesperanzaneta positiva.
Análisis MCP88d7a2fc11844083aff730faeea60018 comprobó PnL/fees portrade ysaldo. Fixedfills/qty+10bpsRTde fricción adicional:net−730.2313USDT; NO esCAGR/DDnuevo.
Cierres-año de trades (NO MTM):2020+181.17,2021+102.41,2022−263.92,2023+155.06,2024−49.31,2025−197.63USDT. Lasfronteras2020/25sonparciales.
Permanenciamediana12h,pausaentretradesmediana64h,63/257reentradasen24h;mejores2trades5.676%delgrossprofit,worsttrade−101.74,best119.83.
## Auditoría V4 del orquestador
Jobecf95de9edc94cb4a8a49241ca6e4ece: ledger/fills/saldoreconciliados.
31/53mesesactivospositivos58.4906%;31/63calendario49.2063%;11/21trimestres52.381%;peormes−2.2818%;DDdaily−5.2132%.
## Decisión
DESCARTAR receta. SinbarrerRSI/media/stopparasustituirfeesporcurvefit. NoportarSPYnicombinarconreferenciaunaesperanzanetaperdedora. No nuevasimulación, framework/live/config. Objetivosnoalcanzados,2026sellado.
