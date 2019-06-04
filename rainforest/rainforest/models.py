from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 500)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "Name: {} Price: {} Description: {}".format(self.name, self.price, self.description)

class Review (models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return "{}, {}".format(self.name, self.date_created)
