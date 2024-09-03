from django.db import models

# Create your models here.
class Order(models.Model):
    title=models.CharField(max_length=200)
    quantity=models.IntegerField()
    description=models.CharField(max_length=200)
    image_url=models.CharField(max_length=2000)
    product_type=models.CharField(max_length=200)