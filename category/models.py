from django.db import models
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length =255, unique =True)
    cat_image =models.ImageField(upload_to='photos/categories', blank =True)

# this following code for customize the name of model in admin panel
    class Meta:
        verbose_name = 'categories'
        verbose_name_plural = 'categories'

    def get_url(self):
         return reverse('products_by_category', args=[self.slug])
    

    def __str__(self):
        return self.category_name





