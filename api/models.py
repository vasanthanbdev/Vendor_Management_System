from django.db import models


# Vendor Model
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['vendor_code']
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Vendor Code: {self.vendor_code}"
    

# Purchase Order Model
class PurchaseOrder(models.Model):
    STATUS_CHOICES =[
        ('Pending', 'Pending'),
        ('Acknowledged', 'Acknowledged'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(max_length=20, default=0.0)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgement_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['po_number']
        
    def __str__(self) -> str:
        return f"Purchase Order Number: {self.po_number}"
    
    
# Vendor Performance Model
# class Performance(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     on_time_delivery_rate = models.FloatField(max_length=20)
#     quality_rating_avg = models.FloatField(max_length=20)
#     average_response_time = models.FloatField(max_length=20)
#     fullfillment_rate = models.FloatField(max_length=20)
    
#     class Meta:
#         verbose_name = 'Vendor Performance'