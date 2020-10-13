from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from .models import User, Stock, Transaction, PF_Value_Daily
from datetime import date


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

    #userinformation
    userinformation = User.objects.values()
    stocks = Stock.objects.all()
    context = {'userinformation':userinformation,'stocks':stocks}
    counter = 0
    for stock in stocks:
        url = ("https://financialmodelingprep.com/api/v3/profile/"+stock.ticker+"?apikey=07eb8824ce1236dcbba7f02dca51447f")
        json_response = get_jsonparsed_data(url)
        extracted = json_response[0]
        stockprice = extracted["price"]
        stocks[counter].value =stockprice
        stocks[counter].save()
        ++counter



    context = {'userinformation':userinformation,'stocks':stocks}
   
    if request.method =='POST':
        stocksearch = request.POST["ticker"]
        url = ("https://financialmodelingprep.com/api/v3/profile/"+stocksearch+"?apikey=07eb8824ce1236dcbba7f02dca51447f")
        json_response = get_jsonparsed_data(url)
        if  json_response:
            extracted = json_response[0]
            stockname = extracted["symbol"]
        else:
            status = 'search_failed'
            
            context = {'userinformation':userinformation,'stocks':stocks,'status':status}
        
######################SEARCH#############################################################################################
        if 'search' in request.POST and json_response:
            today = date.today()
            d3 = today.strftime("%m/%d/%y")
            print("Today's date:", today)
            df= get_data(stockname, start_date="01/01/2015", end_date=d3, index_as_date = True, interval="1wk")
            df['close'].plot()
            plt.figure(figsize=(10,10))
            plt.plot(df.index, df['close'])
            plt.xlabel("date")
            plt.ylabel("$ price")
            plt.title(stockname+ " Stock Price 2015  - 2020")
            plt.savefig("trading/static/trading/stock.png")
            status = "search"
            context = {'extracted':extracted,'userinformation':userinformation,'stocks':stocks,'status':status}        
###########################BUY#########################################################################################
        elif 'buy' in request.POST and json_response:
            extracted = json_response[0]
            stockname = extracted["symbol"]
            stockliveprice =extracted["price"]
            userinformation = User.objects.filter(name="Edgar Santana")
            mystocks = Stock.objects.filter(ticker=stockname)
            today = date.today().strftime('%Y-%m-%d')
            

            for user in userinformation:
                if user.balance >= extracted["price"]:
                    counter = 0
                    found = False
                    counter=0
                    for stock in mystocks:
                        if stock.quantity > 0 and stock.ticker==stockname:
                            found = True
                        else:
                            found = False
                        ++counter
                    if found:
                        mystocks[counter].quantity += 1
                        mystocks[counter].save()
                        status = "buy"
                        t = Transaction(transaction_type='P',transaction_value=stockliveprice,stock_sold=stockname,date=today)
                        t.save()
                    if found == False:
                        n = Stock(ticker = stockname,quantity=1,value=stockliveprice)
                        n.save()
                        status = "buy"
                    userinformation[0].balance -= extracted["price"]
                    userinformation[0].save()
                    t = Transaction(transaction_type='P',transaction_value=stockliveprice,stock_sold=stockname,date=today)
                    t.save()
                else:
                    status = "buy_failed"
                stocks = stocks = Stock.objects.all()
                
                context = {'extracted':extracted,'userinformation':userinformation,'stocks':stocks,'status':status}
                    
            
            
    #############################SELL######################################################################################
        elif 'sell' in request.POST and json_response:
            extracted = json_response[0]
            stockname = extracted["symbol"]
            stockliveprice =extracted["price"]
            userinformation = User.objects.filter(name="Edgar Santana")
            stocks = Stock.objects.filter(ticker=stockname)
            today = date.today().strftime('%Y-%m-%d')
            
            
            
            for user in userinformation:
                    counter = 0
                    found = False
                    counter=0
                    for stock in stocks:
                        if stock.quantity > 1 and stock.ticker==stockname:
                            found = True
                            stocks[counter].quantity -= 1
                            stocks[counter].save()
                            status = "sell"
                            t = Transaction(transaction_type='S',transaction_value=stockliveprice,stock_sold=stockname,date=today)
                            t.save()
                            

                        elif stock.quantity == 1 and stock.ticker == stockname:
                            found = True
                            stocks[counter].delete()
                            
                            
                        ++counter
                    if found:
                        userinformation[0].balance += extracted["price"]
                        userinformation[0].save()
                        status = "sell"
                        t = Transaction(transaction_type='S',transaction_value=stockliveprice,stock_sold=stockname,date=today)
                        t.save()
                        
                    if found == False:
                        status = "sell_failed"
                        
                        
            stocks = Stock.objects.all()
            context = {'extracted':extracted,'userinformation':userinformation,'stocks':stocks,'status':status}






    #Will always be returned
    return render(request,'home.html',context)




        
        
    
       
    
        
def transactionhistory(request):
    transactionrecords = Transaction.objects.all()
    values = PF_Value_Daily.objects.all()
    graphv = {}
    
    for dates in values:
        graphv[dates.date_ending] = dates.value
        date = dates.value
    
    plt.bar(range(len(graphv)), list(graphv.values()), align='center')
    plt.xticks(range(len(graphv)))
    # # for python 2.x:
    # plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
    # plt.xticks(range(len(D)), D.keys())  # in python 2.x

    plt.savefig("trading/static/trading/transaction.png")

    return render(request,'transactionhistory.html',{'transactionrecords':transactionrecords})
    


    
def about(request):
    uname = User.objects.values()
    return render(request,'about.html',{'uname':uname})
    



  
def userinfo(request):
    aml_videos = Stock.objects.all()
    context = {'aml_videos': aml_videos}
    return render(request, "userinfo.html", context)


   
    

def addstock(request):
    return render(request,'addstock.html',{})




    