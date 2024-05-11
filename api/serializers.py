from rest_framework import serializers
from .models import Vendor, PurchaseOrder
    

# Vendor Serializer
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_details', 'address', 'vendor_code']


# Serializes the Performance parameters
class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate'] 
        

# Purchase Order Serializer
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        
   
# Serializer for Acknowlegement date 
class AcknowledgementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgement_date'] 