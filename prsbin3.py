from binance.client import Client
from binance.exceptions import BinanceAPIException
import time

b_api_key = 'xxxxxxxxx'
b_api_secret_key = 'xxxxxxxxxxx'
client = Client(b_api_key, b_api_secret_key)
symbol = 'XRPUSDT'
prices = client.futures_mark_price(symbol=symbol)
max_price = prices.price


def main():
    global prices
    global max_price

    while True:
        prices = client.futures_mark_price(symbol=symbol)
        current_price = prices.price

        if current_price <= max_price * 0.99:
            print("Price dropped on 1% or more from max price in last hour")
            max_price = current_price

        time.sleep(1)


def worker():
    try:
        main()
    except BinanceAPIException as err:
        print(err.status_code)
        print(err.message)
        time.sleep(30)
    finally:
        worker()


if __name__ == "__main__":
    worker()