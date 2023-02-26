from rest_framework import serializers
from .models import Category, Item, Cart, CartItem, StaffPick, StaffPickItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'categoryDesc')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description', 'category_id', 'image_path')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'total', 'created_at', 'updated_at', 'user_id')
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'cart_id', 'item_id')

class StaffPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPick
        fields = ('id', 'name')

class StaffPickItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPickItem
        fields = ('id', 'item_id', 'staffPick_id')


        