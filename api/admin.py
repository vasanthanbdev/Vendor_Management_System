from django.contrib import admin
from .models import Vendor, PurchaseOrder

# Registering Models 
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
