from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    title=models.CharField(max_length=200)
    quantity=models.IntegerField()
    description=models.CharField(max_length=200)
    image_url=models.URLField(max_length=2000)
    product_type=models.CharField(max_length=200)
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )