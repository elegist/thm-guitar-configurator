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
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    image = models.ImageField(upload_to='items', null=True, blank=True)

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

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

class ConfigurationItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.item)
    
class Configuration(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    configuration_items = models.ManyToManyField(Item)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_staff_pick = models.BooleanField(default=False)

    def total_price(self):
        configuration_items = self.configuration_items.all()
        total = sum([item.price for item in configuration_items])
        return total

    def __str__(self):
        return self.customer.user.username
    
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Configuration, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.item.price
    
    def total_discount_price(self):
        return self.quantity * self.item.discount_price

    def amount_saving(self):
        return self.total_price - self.total_discount_price

    @property
    def final_price(self):
        if self.item.discount_percentage:
            return self.total_discount_price
        return self.total_price

    def __str__(self):
        return f'{self.quantity} of {self.item}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def total_price(self):
        order_items = self.items.all()
        total = sum([item.final_price() for item in order_items])
        return total
    
    def __str__(self):
        return self.customer.user.username
