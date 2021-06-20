from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_code = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='images/',null=True, blank=True)
    product_description = models.CharField(max_length=2000)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return self.product.product_name

