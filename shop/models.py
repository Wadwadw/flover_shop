from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.BooleanField(default=False)
    brand = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    image = models.ForeignKey('Image', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title

