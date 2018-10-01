import ccxt
from pprint import pprint

pair = 'ETH/BTC'
limit = 3

highLimit = 0.2
lowLimit = 0.001
tol = 10**-10

names = ccxt.exchanges[:200]
# Exchanges = []

bids = {}

for item in names:
    exchange = getattr(ccxt, item)()
    # print(exchange.load_markets())
    try:
        exchange.fetch_order_book(pair, limit)
        exchange.fetch_order_book(pair, limit)
        print(type(exchange))
        # print(item, exchange['bids'])
        # print(item)
        # bidPrice = exchange['bids'][0][0]
        # askPrice = exchange['asks'][0][0]
        # print(bidPrice, askPrice)
        # if bidPrice - highLimit < tol and bidPrice - lowLimit > lowLimit:
        #     bids[item] = bidPrice
        # else:
        #     bids[item] = -1
        # if askPrice - highLimit < tol and askPrice - lowLimit > lowLimit:
        #     asks[item] = askPrice
        # else:
        #     asks[item] = -1

        # print('bbbb')
    except:
        pass
        # print(item + ' not working')
        # print('aaaaa')
    # bidPrice = exchange['bids'][0][0]
    # askPrice = exchange['asks'][0][0]
    # if bidPrice - highLimit < tol and bidPrice - lowLimit > lowLimit:
    #     bids[item] = bidPrice

print()

# for index, exh in enumerate(Exchanges):
#     exh.fetch_order_book(pair, limit)

# print(Exchanges)
# print(names)
# print(exchanges)

# hb = ccxt.huobipro()
# okex = ccxt.okex()

# pair = 'BTC/USDT'
# limit = 3
# Data = [hb.fetch_order_book(pair, limit), okex.fetch_order_book(pair, limit)]
# bids = []
# asks = []
# for data in Data:
#     bids.append(data['bids'][0])
#     asks.append(data['asks'][0])

# print(bids, asks)
# print(1.*bids[0][0] / asks[1][0])
