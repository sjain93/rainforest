from django.forms import ModelForm
from rainforest.models import Product, Review

class Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
