from django.db import models


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class ProductType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Product Types'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, auto_created=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(ProductType, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    views = models.ManyToManyField(Ip, related_name='product_views', blank=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True, upload_to='product_images')

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()




