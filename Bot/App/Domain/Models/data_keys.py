from enum import Enum


# # Keys kunnen gemaakt worden met de generator: /Observer/Overige/interval_generator.py
# class Interval(Enum):
#     _1M = '1m'
#     _5M = '5m'
#     _15M = '15m'
#     _1H = '1h'
#     _4H = '4h'
#     _1D = '1d'
#     _1W = '1w'
#
#
#
# # Keys kunnen gemaakt worden met de generator: /Observer/Overige/symbol_generator.py
# class Symbol(Enum):
#     BTCUSDT = 'BTCUSDT'
#     ETHUSDT = 'ETHUSDT'
#     BNBUSDT = 'BNBUSDT'
#     SOLUSDT = 'SOLUSDT'
#     ADAUSDT = 'ADAUSDT'
#     XRPUSDT = 'XRPUSDT'
#     DOTUSDT = 'DOTUSDT'
#     LINKUSDT = 'LINKUSDT'
#     XMRUSDT = 'XMRUSDT'
#     LTCUSDT = 'LTCUSDT'

# Keys kunnen gemaakt worden met de generator: /Observer/Overige/data_key_generator.py
class Key(Enum):
    BTCUSDT_1M = 'BTCUSDT_1M'
    BTCUSDT_5M = 'BTCUSDT_5M'
    BTCUSDT_15M = 'BTCUSDT_15M'
    BTCUSDT_1H = 'BTCUSDT_1H'
    BTCUSDT_4H = 'BTCUSDT_4H'
    BTCUSDT_1D = 'BTCUSDT_1D'
    BTCUSDT_1W = 'BTCUSDT_1W'
    ETHUSDT_1M = 'ETHUSDT_1M'
    ETHUSDT_5M = 'ETHUSDT_5M'
    ETHUSDT_15M = 'ETHUSDT_15M'
    ETHUSDT_1H = 'ETHUSDT_1H'
    ETHUSDT_4H = 'ETHUSDT_4H'
    ETHUSDT_1D = 'ETHUSDT_1D'
    ETHUSDT_1W = 'ETHUSDT_1W'
    BNBUSDT_1M = 'BNBUSDT_1M'
    BNBUSDT_5M = 'BNBUSDT_5M'
    BNBUSDT_15M = 'BNBUSDT_15M'
    BNBUSDT_1H = 'BNBUSDT_1H'
    BNBUSDT_4H = 'BNBUSDT_4H'
    BNBUSDT_1D = 'BNBUSDT_1D'
    BNBUSDT_1W = 'BNBUSDT_1W'
    SOLUSDT_1M = 'SOLUSDT_1M'
    SOLUSDT_5M = 'SOLUSDT_5M'
    SOLUSDT_15M = 'SOLUSDT_15M'
    SOLUSDT_1H = 'SOLUSDT_1H'
    SOLUSDT_4H = 'SOLUSDT_4H'
    SOLUSDT_1D = 'SOLUSDT_1D'
    SOLUSDT_1W = 'SOLUSDT_1W'
    ADAUSDT_1M = 'ADAUSDT_1M'
    ADAUSDT_5M = 'ADAUSDT_5M'
    ADAUSDT_15M = 'ADAUSDT_15M'
    ADAUSDT_1H = 'ADAUSDT_1H'
    ADAUSDT_4H = 'ADAUSDT_4H'
    ADAUSDT_1D = 'ADAUSDT_1D'
    ADAUSDT_1W = 'ADAUSDT_1W'
    XRPUSDT_1M = 'XRPUSDT_1M'
    XRPUSDT_5M = 'XRPUSDT_5M'
    XRPUSDT_15M = 'XRPUSDT_15M'
    XRPUSDT_1H = 'XRPUSDT_1H'
    XRPUSDT_4H = 'XRPUSDT_4H'
    XRPUSDT_1D = 'XRPUSDT_1D'
    XRPUSDT_1W = 'XRPUSDT_1W'
    DOTUSDT_1M = 'DOTUSDT_1M'
    DOTUSDT_5M = 'DOTUSDT_5M'
    DOTUSDT_15M = 'DOTUSDT_15M'
    DOTUSDT_1H = 'DOTUSDT_1H'
    DOTUSDT_4H = 'DOTUSDT_4H'
    DOTUSDT_1D = 'DOTUSDT_1D'
    DOTUSDT_1W = 'DOTUSDT_1W'
    LINKUSDT_1M = 'LINKUSDT_1M'
    LINKUSDT_5M = 'LINKUSDT_5M'
    LINKUSDT_15M = 'LINKUSDT_15M'
    LINKUSDT_1H = 'LINKUSDT_1H'
    LINKUSDT_4H = 'LINKUSDT_4H'
    LINKUSDT_1D = 'LINKUSDT_1D'
    LINKUSDT_1W = 'LINKUSDT_1W'
    XMRUSDT_1M = 'XMRUSDT_1M'
    XMRUSDT_5M = 'XMRUSDT_5M'
    XMRUSDT_15M = 'XMRUSDT_15M'
    XMRUSDT_1H = 'XMRUSDT_1H'
    XMRUSDT_4H = 'XMRUSDT_4H'
    XMRUSDT_1D = 'XMRUSDT_1D'
    XMRUSDT_1W = 'XMRUSDT_1W'
    LTCUSDT_1M = 'LTCUSDT_1M'
    LTCUSDT_5M = 'LTCUSDT_5M'
    LTCUSDT_15M = 'LTCUSDT_15M'
    LTCUSDT_1H = 'LTCUSDT_1H'
    LTCUSDT_4H = 'LTCUSDT_4H'
    LTCUSDT_1D = 'LTCUSDT_1D'
    LTCUSDT_1W = 'LTCUSDT_1W'

    @classmethod
    def create_key(cls, symbol, interval) -> str:
        if isinstance(symbol, Symbol) and isinstance(interval, Interval):
            key = f"{symbol.value.upper()}_{interval.value.upper()}"
        elif isinstance(symbol, str) and isinstance(interval, str):
            key = f"{symbol.upper()}_{interval.upper()}"
        else:
            raise TypeError("Key is niet juist type")
        return key


