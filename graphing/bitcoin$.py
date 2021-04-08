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

        x = time
        y = rate

        # use the plot function
        plt.plot(x , y)

        # show the graph
        plt.show()
        plt.plot(hourly_perf_total)
        plt.xticks(np.arange(0, n_results + 1, 24.0))
        plt.ylabel('Current Price')
        plt.xlabel('Time')
        title = 'Bitcoin Price Updates'
        plt.title(title)

        # log y axis
        plt.semilogy()
        plt.grid(True)

        plt.show()





main()
