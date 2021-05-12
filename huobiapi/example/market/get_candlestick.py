from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.utils import *

market_client = MarketClient(init_log=True)
interval = CandlestickInterval.DAY1
symbol = "ethusdt"
list_obj = market_client.get_candlestick(symbol, interval, 2)
LogInfo.output("---- {interval} candlestick for {symbol} ----".format(interval=interval, symbol=symbol))
LogInfo.output_list(list_obj)
















