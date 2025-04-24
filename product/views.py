from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from product.models import Product
# from product.serializers import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    data = {'foo': 'bar'}
    return Response({"message": "Hello, API!"})

def add(request):
    return HttpResponse("ADD productts.")

