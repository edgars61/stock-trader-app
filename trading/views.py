from django.shortcuts import render
from django.http import HttpResponse

#plotting
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt





# Create your views here.


from yahoo_fin.stock_info import *

#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)





def home(request):
    url = ("https://financialmodelingprep.com/api/v3/search?query=alphabet&limit=1&exchange=NASDAQ&apikey=demo")
  
    search = get_jsonparsed_data(url)[0]["symbol"]
    df= get_data(search, start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")
    

    df['close'].plot()
    plt.figure(figsize=(10,10))
    plt.plot(df.index, df['close'])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title(search+ " Stock Price 1/1/17 - 8/1/19")
    plt.savefig("trading/static/trading/foo.png")

    return render(request,'home.html')