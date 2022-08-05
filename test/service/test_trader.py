from datetime import datetime

from src.service.trader import Trader
from src.service.reporter import Reporter
from src.service.trade_finder import TradeFinder

from src.repository.trade_repository import TradeRepository

from fixture.trade import trade_create_buy
from fixture.prediction import load_predictions

trader = Trader()
reporter = Reporter()
trade_finder = TradeFinder()
trade_repository = TradeRepository()


def test_trade_buy_many():
    data = load_predictions()
    df = reporter.report_build(data=data)
    df_best = trade_finder.pick_best_options(df, diff=0, rsi=70)
    buy_time = datetime.utcnow()

    trades = trader.trade_buy_many(
        df=df_best,
        limit=2,
        interval='1h',
        buy_time=buy_time,
    )

    assert trades[0].asset == 'BTC'
    # assert trades[1].asset == 'ONT'

    # assert trades[0].buy_price == 0.2521
    # assert trades[0].diff_predicted == 0.1535
    # assert trades[0].buy_quantity == 3966.6799
    # assert trades[0].trades == 47.0

    assert trades[0].buy_price == 20977.69
    assert trades[0].diff_predicted == 1.0215
    assert trades[0].buy_quantity == 0.0477
    assert trades[0].trades == 3703.0



def test_trade_buy_1h():
    now = datetime.utcnow()
    asset = 'BTC'
    market = 'USDT'
    interval = '1h'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.utcnow()

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id
    assert trade_buy.buy_price == 10000
    assert trade_buy.buy_quantity == 0.001
    assert trade_buy.diff_predicted == 0.00001
    assert trade_buy.trades == 10000
    assert trade_buy.interval == '1h'
    assert trade_buy.interval_start.hour == now.hour + 1

    assert trade_buy.buy_order == {}

    assert trade_buy.interval_start.minute == 0
    assert trade_buy.interval_start.second == 0
    assert trade_buy.interval_end.minute == 0
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_13():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:13:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 15
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 12
    assert trade_buy.interval_end.minute == 30
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_0():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:00:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 15
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 12
    assert trade_buy.interval_end.minute == 30
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_15():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:15:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 30
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 12
    assert trade_buy.interval_end.minute == 45
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_30():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:30:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 45
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 13
    assert trade_buy.interval_end.minute == 0
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_45():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:45:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 13
    assert trade_buy.interval_start.minute == 0
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 13
    assert trade_buy.interval_end.minute == 15
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_28():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:28:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 30
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 12
    assert trade_buy.interval_end.minute == 45
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_43():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:43:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 45
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 13
    assert trade_buy.interval_end.minute == 0
    assert trade_buy.interval_end.second == 0

def test_trade_buy_15m_58():
    asset = 'BTC'
    market = 'USDT'
    interval = '15m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:58:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 13
    assert trade_buy.interval_start.minute == 0
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 13
    assert trade_buy.interval_end.minute == 15
    assert trade_buy.interval_end.second == 0


def test_trade_buy_5m_0():
    asset = 'BTC'
    market = 'USDT'
    interval = '5m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:00:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 12
    assert trade_buy.interval_start.minute == 5
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 12
    assert trade_buy.interval_end.minute == 10
    assert trade_buy.interval_end.second == 0

def test_trade_buy_5m_55():
    asset = 'BTC'
    market = 'USDT'
    interval = '5m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.strptime('09/19/19 12:55:00', '%m/%d/%y %H:%M:%S')

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        interval=interval,
        trades=trades,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id

    assert trade_buy.interval_start.hour == 13
    assert trade_buy.interval_start.minute == 0
    assert trade_buy.interval_start.second == 0

    assert trade_buy.interval_end.hour == 13
    assert trade_buy.interval_end.minute == 5
    assert trade_buy.interval_end.second == 0


def test_trade_buy_30m():
    asset = 'BTC'
    market = 'USDT'
    interval = '30m'
    trades = 10000
    price = 10000
    diff = 0.00001
    quantity = 0.001
    buy_time = datetime.utcnow()

    trade_buy = trader.trade_buy(
        buy_time=buy_time,
        asset=asset,
        market=market,
        trades=trades,
        interval=interval,
        price=price,
        diff=diff,
        quantity=quantity,
    )
    trade_last = trade_repository.find_last_trade()

    assert trade_buy.id == trade_last.id
    assert trade_buy.buy_price == 10000
    assert trade_buy.buy_quantity == 0.001
    assert trade_buy.diff_predicted == 0.00001
    assert trade_buy.interval == '30m'

    assert trade_buy.buy_order == {}

    if buy_time.minute > 30:
        assert trade_buy.interval_start.minute == 0
        assert trade_buy.interval_start.second == 0
        assert trade_buy.interval_end.minute == 30
        assert trade_buy.interval_end.second == 0

    if buy_time.minute < 30:
        assert trade_buy.interval_start.minute == 30
        assert trade_buy.interval_start.second == 0
        assert trade_buy.interval_end.minute == 0
        assert trade_buy.interval_end.second == 0


def test_trade_sell():
    trade_buy = trade_create_buy()

    price = trade_buy.buy_price * 0.01 + trade_buy.buy_price

    trader.trade_sell(
        trade=trade_buy,
        price=price,
    )

    trade_sell = trade_repository.find_id(trade_id=trade_buy.id)

    assert trade_sell.sell_price == 10100
    assert trade_sell.sell_order == {}
