from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet

router = DefaultRouter()
router.register(r'api/vendors', VendorViewSet, basename='vendor')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]