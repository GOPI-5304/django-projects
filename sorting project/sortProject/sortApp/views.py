from django.shortcuts import render
from rest_framework import generics
from . models import *
from .serializers import * 
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class productDetails(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=productserializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('product_name','category')
    ordering_fields=('price','id')
    

class feedbackDetails(generics.ListCreateAPIView):
    queryset=feedback.objects.all()
    serializer_class=feedbackserializer