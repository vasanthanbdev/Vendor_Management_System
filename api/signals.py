from django.db.models import F, Q, Count 
from .models import PurchaseOrder
from django.db.models.signals import post_save
from django.dispatch import receiver
        

# reciever funcitons that recieves to model signals for the PurchaseOrder model
@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, created, **kwargs):
    if instance.status == 'Delivered':
        vendor = instance.vendor
        vendor.on_time_delivery_rate = F('on_time_delivery_rate') + 1 / Count('purchaseorder', filter=Q(status='Completed'))
        vendor.quality_rating_avg = (F('quality_rating_avg') * Count('purchaseorder', filter=Q(status='Completed')) + instance.quality_rating) / (Count('purchaseorder', filter=Q(status='Completed')) + 1)
        vendor.fulfillment_rate = F('fulfillment_rate') + 1 / Count('purchaseorder')
        vendor.save()

    if instance.acknowledgment_date:
        vendor = instance.vendor
        vendor.average_response_time = (F('average_response_time') * Count('purchaseorder', filter=Q(acknowledgment_date__isnull=False)) + (instance.acknowledgment_date - instance.issue_date).total_seconds()) / (Count('purchaseorder', filter=Q(acknowledgment_date__isnull=False)) + 1)
        vendor.save()