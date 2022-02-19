def getCoinInfo(coin):
    from data.config import my_binance_api_key, my_binance_api_secret
    from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
    from pycbrf.toolbox import ExchangeRates

    client = Client(my_binance_api_key, my_binance_api_secret)
    all_tickers = client.get_all_tickers()
    rates = ExchangeRates()
    RUB = float(rates["USD"].rate)
    for ticker in all_tickers:
        if ticker["symbol"] == coin + "USDT" or ticker["symbol"] == coin + "BUSD":
            return "\n".join(["coin: " + coin, "Цена в долларах: " + ticker["price"],
                              "Цена в рублях: " + str(float(ticker["price"]) * RUB)])
    return "Wrong symbol"


def getMoreCoinInfo(coin):
    from data.config import my_binance_api_key, my_binance_api_secret
    from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

    client = Client(my_binance_api_key, my_binance_api_secret)
    return client.get_symbol_info(symbol=coin + "USDT")
