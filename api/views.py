from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, PerformanceSerializer, AcknowledgementSerializer
from rest_framework import generics


# Lists all vendors and Create new vendor 
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    
# gives the purticular vendor 
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
     

# Lists the performance metrics of a specific vendor
class PerformanceList(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = PerformanceSerializer    


# list and create purchase orders
class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    

# gives the specific puchase order
class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    
# retrives the acknowledgment date 
class Acknowledgement(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgementSerializer