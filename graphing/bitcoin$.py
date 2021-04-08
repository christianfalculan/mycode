#!/usr/bin/python3

# import requests to perform HTTP GETs and create graph using json data on Bitcoin
import requests
import numpy as np
import matplotlib.pyplot as plt
import json


def main():
    # define API as variable
    api = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # make HTTP GET request, and capture response
    r = requests.get(api)

    # strip the JSON off the 200 response object and map to new variable
    btcdata = r.json()

    # open a file we can write to (not overwrite)
    with open("Bitcoin.data", "a") as btc:
        # btc.write() # this would work just like the line below
        # print("this goes into the file", file=btc)

        # write current timestamp & BTC to USD price from captured data
        # print(btcdata.get("time").get("updated"), file=btc)
        # print(btcdata.get("bpi").get("USD").get("rate"), file=btc)

        time = btcdata.get("time").get("updated")
        rate = btcdata.get("bpi").get("USD").get("rate")

        # print current timestamp
        btc.write(f"{time}\n")
        # print current price of Bitcoin
        btc.write(f"{rate}\n")

        # define graph variables using output from btcdata
        x = time
        y = float(f"{rate}")

        # make the graph
        plt.plot(x, y)

        #stuck ???
        plt.xticks(np.arange(????)

        plt.ylabel('Current Price')
        plt.xlabel('Time')
        plt.ylim(1,70,00)
        plt.xlim(1,8)
        title = 'Bitcoin Price Updates'
        plt.title(title)
        plt.show()





main()
