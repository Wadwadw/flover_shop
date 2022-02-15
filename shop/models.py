from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    sale_price = models.IntegerField()
    sale = models.BooleanField(default=False)
    brand = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title
