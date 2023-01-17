from django.db import models
from django.contrib.auth.models import User
# Create your models here.

## color, wood, frets, pickup, hardware##
class Category(models.Model):
    name = models.CharField(max_length = 150)
    categoryDesc = models.CharField(max_length = 150)

class Item(models.Model):
    name = models.CharField(max_length = 150)
    category = models.ForeignKey(Category, verbose_name="fk_category", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=150)

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="fk_user", on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="fk_cart", on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, verbose_name="fk_item", on_delete=models.CASCADE, null=True)


