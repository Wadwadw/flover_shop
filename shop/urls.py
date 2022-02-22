from django.urls import path
from .views import ProductListView, product_detail


urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<str:slug>/', product_detail, name='product-detail')
]