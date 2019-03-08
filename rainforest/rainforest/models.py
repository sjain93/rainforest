from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    price = models.IntField()

class Review (models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
