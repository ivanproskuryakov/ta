from src.service.backtester import BackTester

from src.parameters import assets, market

backtester = BackTester(
    market=market,
    interval='15m',
)

for asset in assets:
    backtester.run(
        asset=asset,
        model="gru-b-1000-48.keras",
        width=1000
    )
