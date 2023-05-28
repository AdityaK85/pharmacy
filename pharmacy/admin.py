from django.contrib import admin
from .models import *

# Register your models here.

# Register your models here.

@admin.register(CustomerMaster)
class CustomerMasterAdmin(admin.ModelAdmin):
    list_display=['id','customer_name','customer_mobile', 'payment_mode', 'payment_bal', 'created_dt']

@admin.register(MedicineMaster)
class MedicineMasterAdmin(admin.ModelAdmin):
    list_display=['id','medicine_name','batch_no', 'medicine_unit', 'medicine_exp', 'medicine_qty', 'medicine_price', 'created_dt']

@admin.register(BuyMaster)
class BuyMasterAdmin(admin.ModelAdmin):
    list_display=['id', 'fk_customer', 'fk_medicine','discount','tax', 'paid_amt', 'net_total', 'payment_status', 'created_dt']