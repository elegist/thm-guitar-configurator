from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    image = models.ImageField()

    @property
    def discount_price(self):
        discount = self.price / 100 * self.discount_percentage
        price = self.price - discount
        return price
    
    def add_to_cart(self):
        return reverse('add-to-cart', kwargs={
            'item_id': str(self.pk)
        })

    def remove_from_cart(self):
        return reverse('remove-from-cart', kwargs={
            'item_id': str(self.pk)
        })

    def __str__(self):
        return self.name
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.username
    

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