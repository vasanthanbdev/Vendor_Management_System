from rest_framework import serializers
from .models import Vendor, PurchaseOrder, Performance


# Vendor Serializer - Using ModelSerializer from the DRF
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'