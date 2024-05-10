from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_ecommerce.product.serializers import *
from drf_ecommerce.product.models import *

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """

    query_set = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.query_set, many=True)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all brands
    """

    query_set = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.query_set, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products
    """

    query_set = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.query_set, many=True)
        return Response(serializer.data)