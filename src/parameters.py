from binance import Client

DB_ETHEREUM = '/home/ivan/.ethereum/geth/chaindata'
DB_URL = {
    "dev": "postgresql://postgres:@localhost/ta_dev",
}

shift_steps = 4
tail = 100
sequence_length = 100
ASSET = 'BTC'
market = 'USDT'

assets_down = [
    "BTCUP",
    "BTCDOWN",
    "ETHUP",
    "ETHDOWN",
    "ADAUP",
    "ADADOWN",
    "LINKUP",
    "LINKDOWN",
    "BNBUP",
    "BNBDOWN",
    # "TRXUP",
    # "TRXDOWN",
    # "XRPUP",
    # "XRPDOWN",
    # "DOTUP",
    # "DOTDOWN",
]

assets = [
    "BTC",
    "ETH",
    "BNB",
    "NEO",
    "LTC",
    "ADA",
    "XRP",
    "EOS",
    "TUSD",
    "IOTA",
    "XLM",
    "ONT",
    "TRX",
    "ETC",
    "ICX",
    "NULS",
    "VET",
    "USDC",
    "LINK",
    "WAVES",
    "ONG",
    "HOT",
    "ZIL",
    "ZRX",
    "FET",
    "BAT",
    "XMR",
    "ZEC",
    "IOST",
    "CELR",
    "DASH",
    "OMG",
    "THETA",
    "ENJ",
    "MITH",
    "MATIC",
    "ATOM",
    "TFUEL",
    "ONE",
    "FTM",
    "ALGO",
    "GTO",
    "DOGE",
    "DUSK",
    "ANKR",
    "WIN",
    "COS",
    "COCOS",
    "MTL",
    "TOMO",
    "PERL",
    "DENT",
    "MFT",
    "KEY",
    "DOCK",
    "WAN",
    "FUN",
    "CVC",
    "CHZ",
    "BAND",
    "BUSD",
    "BEAM",
    "XTZ",
    "REN",
    "RVN",
    "HBAR",
    "NKN",
    "STX",
    "KAVA",
    "ARPA",
    "IOTX",
    "RLC",
    "CTXC",
    "BCH",
    "TROY",
    "VITE",
    "FTT",
    "EUR",
    "OGN",
    "DREP",
    "TCT",
    "WRX",
    "BTS",
    "LSK",
    "BNT",
    "LTO",
    "AION",
    "MBL",
    "COTI",
    "STPT",
    "WTC",
    "DATA",
    "SOL",
    "CTSI",
    "HIVE",
    "CHR",
    "BTCUP",
    "BTCDOWN",
    "ARDR",
    "MDT",
    "STMX",
    "KNC",
    "REP",
    "LRC",
    "PNT",
    "COMP",
    "SC",
    "ZEN",
    "SNX",
    "ETHUP",
    "ETHDOWN",
    "ADAUP",
    "ADADOWN",
    "LINKUP",
    "LINKDOWN",
    "VTHO",
    "DGB",
    "GBP",
    "SXP",
    "MKR",
    "DCR",
    "STORJ",
    "BNBUP",
    "BNBDOWN",
    "MANA",
    "AUD",
    "YFI",
    "BAL",
    "BLZ",
    "IRIS",
    "KMD",
    "JST",
    "SRM",
    "ANT",
    "CRV",
    "SAND",
    "OCEAN",
    "NMR",
    "DOT",
    "RSR",
    "PAXG",
    "WNXM",
    "TRB",
    "SUSHI",
    "YFII",
    "KSM",
    "EGLD",
    "DIA",
    "RUNE",
    "FIO",
    "UMA",
    "TRXUP",
    "TRXDOWN",
    "XRPUP",
    "XRPDOWN",
    "DOTUP",
    "DOTDOWN",
    "BEL",
    "WING",
    "UNI",
    "NBS",
    "OXT",
    "SUN",
    "AVAX",
    "HNT",
    "FLM",
    "ORN",
    "UTK",
    "XVS",
    "ALPHA",
    "AAVE",
    "NEAR",
    "FIL",
    "INJ",
    "AUDIO",
    "CTK",
    "AKRO",
    "AXS",
    "HARD",
    "DNT",
    "STRAX",
    "UNFI",
    "ROSE",
    "AVA",
    "XEM",
    "SKL",
    "GRT",
    "JUV",
    "PSG",
    "1INCH",
    "REEF",
    "OG",
    "ATM",
    "ASR",
    "CELO",
    "RIF",
    "BTCST",
    "TRU",
    "CKB",
    "TWT",
    "FIRO",
    "LIT",
    "SFP",
    "DODO",
    "CAKE",
    "ACM",
    "BADGER",
    "FIS",
    "OM",
    "POND",
    "DEGO",
    "ALICE",
    "LINA",
    "PERP",
    "RAMP",
    "SUPER",
    "CFX",
    "AUTO",
    "TKO",
    "PUNDIX",
    "TLM",
    "BTG",
    "MIR",
    "BAR",
    "FORTH",
    "BAKE",
    "BURGER",
    "SLP",
    "SHIB",
    "ICP",
    "AR",
    "POLS",
    "MDX",
    "MASK",
    "LPT",
    "XVG",
    "ATA",
    "GTC",
    "TORN",
    "ERN",
    "KLAY",
    "PHA",
    "BOND",
    "MLN",
    "DEXE",
    "C98",
    "CLV",
    "QNT",
    "FLOW",
    "TVK",
    "MINA",
    "RAY",
    "FARM",
    "ALPACA",
    "QUICK",
    "MBOX",
    "FOR",
    "REQ",
    "GHST",
    "WAXP",
    "TRIBE",
    "GNO",
    "XEC",
    "ELF",
    "DYDX",
    "POLY",
    "IDEX",
    "VIDT",
    "USDP",
    "GALA",
    "ILV",
    "YGG",
    "SYS",
    "DF",
    "FIDA",
    "FRONT",
    "CVP",
    "AGLD",
    "RAD",
    "BETA",
    "RARE",
    "LAZIO",
    "CHESS",
    "ADX",
    "AUCTION",
    "DAR",
    "BNX",
    "MOVR",
    "CITY",
    "ENS",
    "KP3R",
    "QI",
    "PORTO",
    "POWR",
    "VGX",
    "JASMY",
    "AMP",
    "PLA",
    "PYR",
    "RNDR",
    "ALCX",
    "SANTOS",
    "MC",
    "BICO",
    "FLUX",
    "FXS",
    "VOXEL",
    "HIGH",
    "CVX",
    "PEOPLE",
    "OOKI",
    "SPELL",
    "JOE",
    "ACH",
    "IMX",
    "GLMR",
    "LOKA",
    "SCRT",
    "API3",
    "BTTC",
    "ACA",
    "ANC",
    "XNO",
    "WOO",
    "ALPINE",
    "T",
    "ASTR",
    "GMT",
    "KDA",
    "APE",
    "BSW",
    "BIFI",
    "MULTI",
    "STEEM",
    "MOB",
    "NEXO",
    "REI",
    "GAL",
    "LDO",
    "EPX",
]

API_KEY = "y95Lhdr2WXTVCbD44gpDhcOHKQaUr1LVNIOFhk1SIhxq4nzCdVoLB0obXWLcyRio"
API_SECRET = "nBmXWlMBreF5uttkRVDxKbEbYtByJiW322iUtGMUCvDsHha9k5tMRjKCSmZtHFsb"

intervals = [
    # Client.KLINE_INTERVAL_1MINUTE,
    # Client.KLINE_INTERVAL_3MINUTE,
    # Client.KLINE_INTERVAL_5MINUTE,
    Client.KLINE_INTERVAL_15MINUTE,
    # Client.KLINE_INTERVAL_30MINUTE,
    #
    # Client.KLINE_INTERVAL_1HOUR,
    # Client.KLINE_INTERVAL_2HOUR,
    # Client.KLINE_INTERVAL_4HOUR,
]

# INTERVAL = Client.KLINE_INTERVAL_1MINUTE
# INTERVAL = Client.KLINE_INTERVAL_3MINUTE
INTERVAL = Client.KLINE_INTERVAL_5MINUTE
# INTERVAL = Client.KLINE_INTERVAL_15MINUTE
# INTERVAL = Client.KLINE_INTERVAL_30MINUTE
# INTERVAL = Client.KLINE_INTERVAL_1HOUR
