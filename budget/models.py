from django.db import models

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