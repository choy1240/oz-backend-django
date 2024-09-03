from django.db import models

# Create your models here.
class ManuBsn(models.Model):
    img_url=models.CharField(max_length=2000)
    bsn_name=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=50)
    ceo_name=models.CharField(max_length=50)
class ManuAccount(models.Model):
    img_url=models.CharField(max_length=2000)
    bank_name=models.CharField(max_length=50)
    account_no=models.CharField(max_length=200)