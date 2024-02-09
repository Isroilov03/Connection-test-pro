from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *



"""  Filter User API   """

@api_view(['GET'])
def filter_user_by_username(request):
    username = request.GET.get('username')
    users = User.objects.filter(username__icontains=username).order_by('-id')
    ser = UserSerializer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_product_by_subcategory(request, pk):
    subcategory = Subcategory.objects.get(pk=pk)
    products = Product.object.filter(subcategory=subcategory).order_by('-id')
    ser = ProductSer(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_product_by_price(request):
    small_amount = request.GET.get('small_amount')
    large_amount = request.GET.get('large_amount')
    products = Product.objects.filter(cost__gte=small_amount, cost__lte=large_amount).order_by('-id')
    ser = ProductSer(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_product_by_price_and_subcategory(request, pk):
    small_amount = request.GET.get('small_amount')
    large_amount = request.GET.get('large_amount')
    products = Product.objects.filter(subcategory_id=pk, cost__gte=small_amount, cost__lte=large_amount).order_by('-id')
    ser = ProductSer(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_product_by_rating(request):
    products = Product.objects.all().order_by('-rating')[:10]
    ser = ProductSer(products, many=True)
    return Response(ser.data)
























