from django.urls import path
from .views import VendorList, VendorDetail, PerformanceList, PurchaseOrderList, PurchaseOrderDetail, Acknowledgement

urlpatterns = [
    path('vendors/', VendorList.as_view()),
    path('vendors/<int:pk>/', VendorDetail.as_view()),
    path('vendors/<int:pk>/performance/', PerformanceList.as_view()),
    path('purchase_orders/', PurchaseOrderList.as_view()),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetail.as_view()),
    path('purchase_orders/<int:pk>/acknowledgement/', Acknowledgement.as_view())
]