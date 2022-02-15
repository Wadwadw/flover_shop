from rest_framework import serializers
from .models import Product, Image


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price',
            'sale_price',
            'sale',
            'brand',
            'product_type',
            'category',
            'rating',
            'views',
            'availability',
            'image',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'title',
            'image',
        )
