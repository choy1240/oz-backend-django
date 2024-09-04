from django.db import models
from django.conf import settings

# Create your models here.
class ManuBsn(models.Model):
    img_url=models.CharField(max_length=2000)
    bsn_name=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=50)
    ceo_name=models.CharField(max_length=50)
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="manu_bsn"
    )
class ManuAccount(models.Model):
    img_url=models.CharField(max_length=2000)
    bank_name=models.CharField(max_length=50)
    account_no=models.CharField(max_length=200)
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="manu_account"
    )