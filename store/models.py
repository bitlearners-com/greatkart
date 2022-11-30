from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name        = models.CharField(max_length=200, unique =True)
    slug                = models.CharField(max_length=200, unique =True)
    description         = models.CharField(max_length=500, unique =True)
    price               = models.IntegerField()
    stock               = models.IntegerField()
    image               = models.ImageField(upload_to='photos/products')   
    is_available        = models.BooleanField(default=True)
    is_available        = models.BooleanField(default=True)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_Date       = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.product_name
