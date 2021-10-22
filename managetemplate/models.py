#from django.contrib.postgres.fields import jsonb, JSONField
from django.db import models

# Create your models here.

class Settings(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    address = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    gas_limit = models.IntegerField()
    slippage = models.FloatField()
    gas_price = models.IntegerField()
    eth_amount = models.IntegerField()
    smart_contract = models.CharField(max_length=100)