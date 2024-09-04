from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    type=models.CharField(max_length=2000, choices=[
        ("CM", "Customer"),
        ("MF", "Manufacturer")
    ])
    manu_product_type=models.CharField(max_length=2000, null=True)