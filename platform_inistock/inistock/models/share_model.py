from enum import Enum

from django.db import models

from inistock.models.person_model import PersonModel


class ShareType(Enum):
    sell = "sell"
    buy = "buy"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class ShareModel(models.Model):
    """Share model
    Represents the information of the share
    """

    share_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    shares = models.IntegerField(null=False, blank=False)
    type = models.CharField(
        max_length=20, choices=ShareType.choices(), default=ShareType.buy.value
    )
    date = models.DateField()
    price = models.FloatField()  # price cost of the share
    amount = models.FloatField()  # total amount paid for shares
    currency = models.CharField(max_length=10)
    note = models.CharField(max_length=1000, null=True)
    person = models.ForeignKey(
        PersonModel, on_delete=models.CASCADE, related_name="person"
    )
