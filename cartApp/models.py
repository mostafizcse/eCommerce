from django.db import models
from mainApp.models import Product
# Create your models here.

class CartList(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartItem')
    quantity = models.IntegerField(default=2, blank=True)

    def __str__(self):
        return self.productId.title