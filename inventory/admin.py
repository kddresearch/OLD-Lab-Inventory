from django.contrib import admin
from .models import Item
from .models import Vendor
from .models import Order
from .models import Location
from .models import Categories
from .models import StockControl

# Register your models here.
admin.site.register(Item)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(Location)
admin.site.register(Categories)
admin.site.register(StockControl)
