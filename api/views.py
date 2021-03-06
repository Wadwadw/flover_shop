from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from shop.models import Product


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)