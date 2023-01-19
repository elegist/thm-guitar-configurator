from django.contrib import admin
from .models import *
# Register your models here.
\

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(StaffPick)
admin.site.register(StaffPickItem)