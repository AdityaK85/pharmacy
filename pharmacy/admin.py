from django.contrib import admin
from .models import *

# Register your models here.

# Register your models here.

@admin.register(CustomerMaster)
class CustomerMasterAdmin(admin.ModelAdmin):
    list_display=['id','customer_name','customer_mobile', 'payment_mode', 'payment_bal']