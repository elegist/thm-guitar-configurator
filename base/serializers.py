from rest_framework import serializers
from .models import User, Customer, Category, Item, Configuration, OrderItem, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )
                
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'price',
            'discount_percentage',
            'image',
            'get_image',
        )

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = (
            'id',
            'name',
            'customer',
            'configuration_items',
            'date_created',
            'date_updated',
            'is_staff_pick',
            'total_price',
        )


        