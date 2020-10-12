from django.contrib import admin
from .models import User, Stock, Transaction, PF_Value_Daily
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display=['ticker']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['transaction_type','transaction_value','stock_sold','date']

@admin.register(PF_Value_Daily)
class DailyValueAdmin(admin.ModelAdmin):
    list_display=['value','date_ending']
