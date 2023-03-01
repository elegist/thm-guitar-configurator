from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    @property
    def total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.total for item in order_items])
        return total

    def __str__(self) -> str:
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self) -> str:
        return self.product.name



# ## color, wood, frets, pickup, hardware##
# class Category(models.Model):
#     name = models.CharField(max_length = 150)
#     categoryDesc = models.CharField(max_length = 150)

#     def __str__(self):
#         return self.name

# class Item(models.Model):
#     name = models.CharField(max_length = 150)
#     category = models.ForeignKey(Category, verbose_name="fk_category", on_delete=models.CASCADE, null=True)
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     description = models.CharField(max_length=150)
#     image_path = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name

# class Cart(models.Model):
#     user = models.ForeignKey(User, verbose_name="fk_user", on_delete=models.CASCADE, null=True)
#     total = models.DecimalField(max_digits=8, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.user

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, verbose_name="fk_cart", on_delete=models.CASCADE, null=True)
#     item = models.ForeignKey(Item, verbose_name="fk_item", on_delete=models.CASCADE, null=True)


# class StaffPick(models.Model):
#     name = models.CharField(max_length = 150)
    
#     def __str__(self):
#         return self.name

# class StaffPickItem(models.Model):
#     staffPick = models.ForeignKey(StaffPick, verbose_name="fk_StaffPick", on_delete=models.CASCADE, null=True)
#     item = models.ForeignKey(Item, verbose_name="fk_item", on_delete=models.CASCADE, null=True)    

#     def __str__(self):
#         item = str(self.item)
#         staffPick = str(self.staffPick)
#         name = staffPick + " " + item
#         return name