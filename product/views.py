from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import PoductSerializer
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = PoductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
