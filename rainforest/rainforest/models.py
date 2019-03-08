from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    price = models.IntField()

    def __str__(self):
        return self.name

class Review (models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return "{}, {}".format(self.name, self.date_created)
