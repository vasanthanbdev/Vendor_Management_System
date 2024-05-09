from .models import Vendor
from .serializers import VendorSerializer
from rest_framework import viewsets, permissions

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly
