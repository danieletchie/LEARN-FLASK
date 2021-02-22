from binance.client import Client
from settings import api_key_new, api_secret_new

client = Client(api_key_new, api_secret_new)
def Buy(symbol,quantity,price):
    buy_order = client.create_order(
    symbol= symbol,
    side="BUY",
    type="LIMIT",
    timeInForce="GTC",
    quantity= quantity,
    price= price)
    return buy_order

def Sell(symbol,quantity,price):
    sell_order = client.order_limit_sell(
        symbol = symbol,
        quantity= quantity,
        price = price
        )
    return sell_order
def Test():
    return "Hello world"