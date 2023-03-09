from rest_framework import serializers
from .models import Category, Item, ConfigurationItem, Configuration, OrderItem, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name',
                  'slug',
                  'category',
                  'price',
                  'discount_percentage',
                  'image',
                  'get_image',)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ConfigurationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationItem
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'


        