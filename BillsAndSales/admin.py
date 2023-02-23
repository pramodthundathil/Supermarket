from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cart)
admin.site.register(CheckoutBill)
admin.site.register(DeliveryAddress)
admin.site.register(BillCalculations)
