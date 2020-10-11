from django.shortcuts import render
from django.http import HttpResponse
#plotting
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
#yahoo finance api import 
from yahoo_fin.stock_info import *
import json
# Create your views here.
#!/usr/bin/env python






def home(request):
    if request.method =='POST':
        ticker = request.POST['ticker']
        try:
            # For Python 3.0 and later
            from urllib.request import urlopen
        except ImportError:
            # Fall back to Python 2's urllib2
            from urllib2 import urlopen
            
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

        url = ("https://financialmodelingprep.com/api/v3/profile/"+ticker+"?apikey=07eb8824ce1236dcbba7f02dca51447f")
        json_response = get_jsonparsed_data(url)
        
        if  json_response:
            extracted = json_response[0]
            ticker = extracted["symbol"]
            df= get_data(ticker, start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")
            df['close'].plot()
            plt.figure(figsize=(10,10))
            plt.plot(df.index, df['close'])
            plt.xlabel("date")
            plt.ylabel("$ price")
            plt.title(ticker+ " Stock Price 1/1/17 - 8/1/19")
            plt.savefig("trading/static/trading/foo.png")
            
            
            
        else:
            extracted = "There was an error with your ticker please try again."
    else:
        extracted = "gay porn"
       
    return render(request,'home_1.html',{'extracted':extracted})
        
        
    


    
    

    