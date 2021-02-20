from django.db import models
from django.db.models.base import Model

# Create your models here.

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=20)
    income = models.IntegerField()
    expenditure = models.IntegerField()
    # credit_cards = []
    
    def __str__(self) -> str:
        return "{}\t{}".format(self.user_id, self.name)

class Budget(models.Model):
    # gubun = 
    price = models.IntegerField()
    date = models.DateField()
    # card = 
    

class MyStock(models.Model):
    ticker = models.CharField(max_length=10, primary_key=True)
    market = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    purchase_price = models.FloatField()
    amount = models.IntegerField()
    purchase_date = models.DateField()

    def __str__(self) -> str:
        return "{}:{}".format(self.market, self.ticker)


