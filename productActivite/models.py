from django.db import models

from mainApp.models import Product
# Create your models here.

class Comporisoon(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comporisoon')
    def __str__(self):
        return self.productId.title