#!/usr/bin/python3

# import requests to perform HTTP GETs and create graph using json data on Bitcoin
import requests
import numpy as np
import matplotlib.pyplot as plt
import json


def apicall():
    """make API call to currentprice.json, return back just the date and price info"""
    # define API as variable
    api = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # make HTTP GET request, and capture response
    r = requests.get(api)

    # strip the JSON off the 200 response object and map to new variable
    btcdata = r.json()

    # write current timestamp & BTC to USD price from captured data
    time = btcdata.get("time").get("updated")
    price = btcdata.get("bpi").get("USD").get("rate")

    # create the dictionary we want to add
    # [{"time": str, "priceUSD": float}]
    btcdict = {"time": time, "priceUSD": price}

    # pass back data to use
    return btcdict

def btcfileread():
    """return the data that we have on file if we do not have any data on file, return an empty list"""
    # TRY to read our file data
    try:
        with open("bitcoin.json", "r") as btc:
            # read the data out of our open file
            btcfiledata = json.load(btc)
    # SHOULD TRY FAIL, return an empty list
    except:
        btcfiledata = []
    # return back our json data OR an empty list
    # print(btcfiledata)
    return btcfiledata

def btcfilewrite(btcfiledata):
    with open("bitcoin.json", "w") as btc:
        # json.dump(data to write out, file to write to)
        json.dump(btcfiledata, btc)
    return

def graphmaker(btcfiledata):
    # init two empty lists
    zdate = []
    zpriceusd = []

    for entry in btcfiledata:
        zdate.append(entry.get("time"))
        zpriceusd.append(entry.get("priceUSD"))

    plt.plot(zdate, zpriceusd)
    plt.title('BitCoin Price in USD per Time (BTC Price Updates)')
    plt.xlabel('Date')
    plt.ylabel('Price of BTC in USD')
    plt.savefig("/home/student/static/bitcoin_data.png")

def main():
    """runtime code"""
    # make our API call, and get back JUST the data we want
    btcdata = apicall()
    # return back the current BTC price data we have on file
    btcfiledata = btcfileread()
    # take our dictionary and append it to our current data blob
    btcfiledata.append(btcdata)
    # write our data out
    btcfilewrite(btcfiledata)
    # build our graph
    graphmaker(btcfiledata)
   
    print("Graph created.")

    
main()
