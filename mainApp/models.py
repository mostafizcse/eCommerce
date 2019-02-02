from django.db import models

from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=25, blank=True, null= True)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    sub_name = models.CharField(max_length=35)
    def __str__(self):
        return self.sub_name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='slug')
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    new_price = models.IntegerField()
    old_price = models.IntegerField(blank=True)
    description = models.TextField()

    image = models.FileField(upload_to='product', blank=True, null=True)
    def __str__(self):
        return self.title

class ProductImages(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.FileField(upload_to='product')
    def __str__(self):
        return self.productId.title

class BannerSlider(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='BannerSlider')
    subTitle = models.CharField(max_length=200)
    title = models.CharField(max_length=150)
    details = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    def __str__(self):
        return self.title

class HotDeal(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer = models.CharField(max_length=10)
    deal_time = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    def __str__(self):
        return self.productId.title

class TodayDeal(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer = models.CharField(max_length=10)
    deal_time = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    def __str__(self):
        return self.productId.title

class SpeacialDeal(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.productId.title