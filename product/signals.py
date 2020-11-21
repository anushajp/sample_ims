import logging

from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import Product
from . import constants

logger = logging.getLogger('application_log')


@receiver(post_save, sender=Product)
def product_update(sender, created, **kwargs):
    product = kwargs.get('instance')
    if not created:
        print('Product updated')
        if product.quantity <= constants.NOTIFY_ADMIN_PRODUCT_LIMIT:
            print("Product Quanity reached the minimum")
            # ToDo Create an async task to notify admin
    return
