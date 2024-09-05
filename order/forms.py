from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'quantity', 'description', 'image_url', 'product_type', 'user']
