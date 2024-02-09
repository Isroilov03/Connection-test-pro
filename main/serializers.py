from .models import *
from rest_framework import serializers



class Order_singleSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order_single_product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class ProductSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = "__all__"