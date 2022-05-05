from binance import Client

assets = [
    # "BTC", "ETH",

    "BNB", "ADA", "ROSE", "SOL", "XRP",

    # "DOT", "ATOM", "HBAR", "IOTA", "AVAX",
    # "COTI", "NEAR", "BAT", "WAVES", "MINA",
    # "EGLD", "XTZ", "ALGO", "LUNA", "KSM",
    # "MATIC", "ONE", "1INCH", "KAVA", "OCEAN",
    # "GRT", "ROSE", "CTSI", "ZRX", "TRX",
    # "ETC", "BCH", "LINK", "FIL", "UNI",
    # "GTC", "NU", "POND", "CELO"
]

market = 'USDT'

intervals = [
    Client.KLINE_INTERVAL_1MINUTE,
    Client.KLINE_INTERVAL_3MINUTE,
    Client.KLINE_INTERVAL_5MINUTE,
    Client.KLINE_INTERVAL_15MINUTE,
    Client.KLINE_INTERVAL_30MINUTE,
    Client.KLINE_INTERVAL_1HOUR,
    Client.KLINE_INTERVAL_4HOUR,
    Client.KLINE_INTERVAL_12HOUR,
    Client.KLINE_INTERVAL_1DAY,
]

start_at = '6 month ago UTC'

ASSET = 'ETH'
INTERVAL = Client.KLINE_INTERVAL_1MINUTE
SIZE_SHIFT = 1
SIZE_BATCH = 50
SIZE_INPUT_LABEL = 30
