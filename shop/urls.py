from django.urls import path
from .views import hello, ProductListView


urlpatterns = [
    path('test/', hello, name='hello'),
    path('list/', ProductListView.as_view(), name='product-list')
]