from django.forms import ModelForm
from rainforest.models import Product, Review
from django.core.exceptions import ValidationError

class Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
    
    def clean(self):
        super().clean()
        description = self.cleaned_data.get('description')
        if len(description) < 10 or len(description) > 500:
            raise ValidationError('The description must be between 10-500 characters')


class Review_Form(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'description']
