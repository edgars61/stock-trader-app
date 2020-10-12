from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField(default=1000.00)
    transactions = models.ManyToManyField('Transaction',blank=True)
    stocks = models.ManyToManyField('Stock',blank=True)
    pf_value = models.ManyToManyField('PF_Value_Daily',blank = True)
    def __self__(self):
       return self.name

class Stock(models.Model):
    ticker = models.CharField(max_length=10)

class Transaction(models.Model):
    TRANSACTION_CHOICES =[('P','Purchase'),('S','Sell')]
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_CHOICES)
    transaction_value = models.FloatField(default=0.0)
    stock_sold = models.CharField(max_length=10)
    date = models.DateTimeField() 
    

class PF_Value_Daily(models.Model):
    value = models.FloatField(default=0.0)
    date_ending = models.DateTimeField()