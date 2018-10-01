import ccxt

okcoin = ccxt.okcoinusd()
markets = okcoin.load_markets()
print(okcoin.id, okcoin.symbols)
pair = 'BTC/USD'

#a = okcoin.markets['BTC/USD']
#print(a)


print(okcoin.fetch_ticker(pair))
print("\n====================\n")
print(okcoin.fetch_trades(pair))
