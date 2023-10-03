from rest_framework import serializers
from .models import Cart, CartDetail, Order, OrderDetail


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        Model=CartDetail
        fields='__all__'

class CartSerializers(serializers.ModelSerializer):
    cart_detail=CartDetailSerializer(many=True)
    class Meta:
        model=Cart
        fields='__all__'



