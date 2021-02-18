from binance.client import Client
# from settings import api_key_new, api_secret_new
# import settings as s
from functions import Buy, Sell
import time
# Insert API and Secret key in quotation mark


def Current(api_key, secret_key, product, quantity, margin_p, sell_p, trades):
    while True:
        try:
            client = Client(api_key, secret_key)
            current_symbol = product
            open_orders = client.get_open_orders(symbol=current_symbol)
            btc_balance = client.get_asset_balance(asset="BTC")
            usdt_balance = client.get_asset_balance(asset="USDT")
            # all_orders = client.get_all_orders(symbol=current_symbol)

            buy_id = []
            sell_id = []

            counter = 0
            print(len(open_orders))
            print(open_orders)

            # for order in open_orders:
            #     cancel_or = client.cancel_order(symbol=current_symbol, orderId=order["orderId"])

            open_orders = client.get_open_orders(symbol=current_symbol)
            print(f"Welcome your BTC balance is {btc_balance}")
            print(f"Your USDT balance is {usdt_balance}")
            print(f"You have {len(open_orders)} Open Order")
            while counter < trades:
                open_orders = client.get_open_orders(symbol=current_symbol)
                print(f"starting running counter = {counter}")
                btc_price = client.get_symbol_ticker(symbol=current_symbol)
                btc_price = float(btc_price["price"])
                if len(open_orders) < 1:
                    print(btc_price)
                    print(
                        f"Started calculating buy order count currently at {counter}")
                    buy_price = btc_price - (btc_price * margin_p)
                    buy_price = round(buy_price, 2)
                    buy_order = Buy(current_symbol, quantity, buy_price)
                    print(buy_price)
                    buy_id.append(buy_order['orderId'])
                    counter += 1
                    print(len(buy_id))
                    continue
                else:
                    print("you still have one open order kindly wait or exit")
                    time.sleep(30)
                if len(buy_id) > 0:
                    print("Initing sell order")
                    for id in buy_id:
                        print("Looping through buy order id")
                        order = client.get_order(symbol=current_symbol, orderId=id)
                        while True:
                            try:
                                order = client.get_order(symbol=current_symbol, orderId=id)
                                print("check buy order status ")
                                if order['status'] == "FILLED":
                                    print(f"Calculating Sell Price")
                                    order_price = float(order["price"])
                                    sell_price = order_price + (order_price * sell_p)
                                    sell_price = round(sell_price, 2)
                                    sell_qty = float(order["origQty"])
                                    sell_order = Sell(current_symbol, sell_qty, sell_price)
                                    sell_id.append(sell_order["orderId"])
                                    counter += 1
                                    print(sell_id)
                                    print(
                                        f"Successfully Placed Sell order at {sell_price}")
                                    break
                            except Exception:
                                print("There was an error retrying soon ")
                                continue
                            time.sleep(20)

                    break
        except Exception as e:
            print(f"{e} \n There was an error retryin ASAP")
            time.sleep(10)
            continue
        break

# while trades <= 3:
#     open_orders = client.get_open_orders(symbol='BTCUSDT')
#     btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
#     btc_bal = client.get_asset_balance(asset="BTC")
#     if len(open_orders) < 3:
#         btc_price = float(btc_price['price'])
#         buy_price = btc_price - (btc_price * margin_percent)
#         print(btc_price)
# Current("kYxAXqc5F1q6WKdwCgn6erWaWo2sAf2k8iK8xawEIVPOel2oBmTTisjwf6DavQRe", "LqLDBStDa1BPACEQ1Dryml1zQTWS8YMmnsvkLDoUhPNpjPHtoptaBPrbDTFgQHCL", "BTCUSDT", 0.02, 0.04, 2)
