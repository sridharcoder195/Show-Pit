from django.db import models
from django.template.defaultfilters import slugify

from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get(self):
        return reverse('product',args=[self.slug])


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to='product_images')
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    def get_urls(self):
        return reverse('product',args=[self.cat.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
