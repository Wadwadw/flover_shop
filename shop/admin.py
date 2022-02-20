from django.contrib import admin
from .models import Product, Category, ProductType, Brand, Ip


@admin.register(Ip)
class AdminIpModel(admin.ModelAdmin):
    list_display = ["ip"]


@admin.register(Category)
class AdminCategoryModel(admin.ModelAdmin):
    list_display = ["title", "slug"]


@admin.register(Product)
class AdminProductModel(admin.ModelAdmin):
    list_display = [
        "title",
        "price",
        "sale_price",
        "sale",
        "rating",
        "availability",
    ]
    list_editable = ("price", "sale_price", "sale", "availability")


@admin.register(Brand)
class AdminBrandModel(admin.ModelAdmin):
    list_display = ["title", "slug"]


@admin.register(ProductType)
class AdminProductTypeModel(admin.ModelAdmin):
    list_display = ["title", "slug"]
