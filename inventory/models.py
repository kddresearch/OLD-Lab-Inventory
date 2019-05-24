from django.db import models

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=200)
    cost_per_item = models.IntegerField()
    item_discontinued = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

class Vendor(models.Model):
    description = models.CharField(max_length=200)
    

class Order(models.Model):
    reorder = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)

