from django.contrib import admin
from .models import *

# Register your models here.
class BurgerAdmin(admin.ModelAdmin):
    list_display = ('BurgerID','BurgerName', 'Description','Price', 'PriceM', 'Image', 'Ingredients', 'Category', 'Calories', 'Rating')

admin.site.register(Burgers, BurgerAdmin)


class AddOnsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(AddOns, AddOnsAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('OrderID', 'note', 'order_data')
    
admin.site.register(Orders, OrdersAdmin)