from django.db import models

# Create your models here.
class Burgers(models.Model):
    BurgerID = models.AutoField(primary_key=True)
    BurgerName = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    PriceM = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Image = models.URLField()
    Ingredients = models.TextField()
    Category = models.CharField(max_length=50, blank=True, null=True)
    Calories = models.IntegerField(blank=True, null=True)
    Rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

class AddOns(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    note = models.TextField(default="")
    order_data = models.TextField(default="")

    