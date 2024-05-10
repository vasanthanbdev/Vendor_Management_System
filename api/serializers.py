from rest_framework import serializers
from .models import Vendor


# Vendor Serializer - Using ModelSerializer from the DRF
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_details', 'address', 'vendor_code']
        
