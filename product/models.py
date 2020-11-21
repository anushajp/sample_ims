import os

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()

    is_draft = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProductRequest(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    price_per_unit = models.FloatField()

    amount = models.FloatField()

    is_approved = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
