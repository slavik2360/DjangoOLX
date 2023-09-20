from django.contrib import admin

# Register your models here.
from .models import (
    Product,
    Order
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    ProductAdmin admin.
    """
    readonly_fields = ()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Order admin.
    """
    readonly_fields = ()