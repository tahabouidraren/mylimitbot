import ccxt

print("******************************************")
print("All copyrights belong to @tahabouidraren in IG")
print("******************************************")
print()
first_name = input("Kindly input your first name: ")
print()
print("Welcome to MyLimitBot1.0 " + first_name.capitalize())
print()
platform = input("Please specify which platform you want to trade with? [Example(Binance, Phemex)]: ")
api_key = input("Your platform ApiKey: ")
secret_key = input("Your platform SecretKey: ")
if platform.upper() == 'BINANCE':
    binance = ccxt.binance ({
    'enableRateLimit' : True,
    'apiKey' : api_key,
    'secret' : secret_key,
     })

    wanted_symbol = input("Enter the currency you want to trade in [Example(BTC,ETH...)}: ")
    used_symbol = input("Enter the currency you want to trade with [Example(USDT,USD...)]: ")


    def get_bid_ask():

        btc_phe_book = binance.fetch_order_book(wanted_symbol.upper() + '/' + used_symbol.upper())
        btc_bid = btc_phe_book['bids'][0][0]
        btc_ask = btc_phe_book['asks'][0][0]
        print(f'the best bid: {btc_bid} the best ask: {btc_ask}')
        return btc_bid, btc_ask


    symbol = wanted_symbol.upper() + '/' + used_symbol.upper()
    pos_size = input("Input the amount: ")
    mybid = get_bid_ask()[0]
    params = {}
    choice = input("Are you sure you want to procced with this order of " + pos_size + " " + used_symbol.upper() + " in the " + symbol + " market ? [Yes/No]: ")
    if choice.upper() == 'YES':
        binance.create_limit_buy_order(symbol, pos_size, mybid, params)
        print('Congrats you just made your order of' + str(pos_size))
    else:
        print("Your order has been canceled upon request")
        exit()
elif platform.upper() == 'PHEMEX':
    phemex = ccxt.phemex ({
    'enableRateLimit' : True,
    'apiKey' : api_key,
    'secret' : secret_key,
     })

    wanted_symbol = input("Enter the currency you want to trade in [Example(BTC,ETH...)}: ")
    used_symbol = input("Enter the currency you want to trade with [Example(USDT,USD...)]: ")


    def get_bid_ask():

        btc_phe_book = phemex.fetch_order_book(wanted_symbol.upper() + '/' + used_symbol.upper())
        btc_bid = btc_phe_book['bids'][0][0]
        btc_ask = btc_phe_book['asks'][0][0]
        print(f'the best bid: {btc_bid} the best ask: {btc_ask}')
        return btc_bid, btc_ask


    symbol = wanted_symbol.upper() + '/' + used_symbol.upper()
    pos_size = input("Input the amount: ")
    mybid = get_bid_ask()[0]
    params = {}
    choice = input("Are you sure you want to procced with this order of " + pos_size +' '+ used_symbol.upper() + " in the " + symbol + " market ? [Yes/No]: ")
    if choice.upper() == 'YES':
        phemex.create_limit_buy_order(symbol, pos_size, mybid, params)
        print('Congrats you just made your order of' + str(pos_size))
    else:
        print("Your order has been canceled upon request")
        exit()
print()
print("******************************************")
print("All copyrights belong to @tahabouidraren in IG")
print("******************************************")
print()
