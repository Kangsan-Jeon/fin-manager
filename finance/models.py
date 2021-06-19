from django.db import models
from django.db.models.base import Model
from users import models as user_model

# Create your models here.

class Budget(models.Model):
    BUDGET_CHOICES = (
        ("income", "수입"),
        ("expense", "지출")
    )

    CARD_CHOICES = (
        ("NO", "해당없음"),
        ("SH", "신한"),
        ("WR", "우리"),
        ("SS", "삼성"),
        ("KM", "국민")
    )

    # owner = models.ForeignKey(
    #     user_model.User,
    #     null=True,
    #     on_delete=models.CASCADE,
    #     related_name='budget_owner'
    # )
    gubun = models.CharField(max_length=7,
        choices=BUDGET_CHOICES, 
        default="income"
    )
    price = models.IntegerField()
    date = models.DateField()
    card = models.CharField(max_length=2,
        default="NO",
        choices=CARD_CHOICES
    )

class MyStock(models.Model):
    CURRENCY_CHOICES = (
        ("USD", "USD"),
        ("KRW", "KRW")
    )
    # owner = models.ForeignKey(
    #     user_model.User,
    #     null=True,
    #     on_delete=models.CASCADE,
    #     related_name='mystock_owner'
    # )
    ticker = models.CharField(max_length=10, primary_key=True)
    market = models.CharField(max_length=10)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")
    purchase_price = models.FloatField()
    amount = models.IntegerField()
    purchase_date = models.DateField()

    def __str__(self) -> str:
        return "{}:{}".format(self.market, self.ticker)


