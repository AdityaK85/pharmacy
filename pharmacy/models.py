from django.db import models
# user : pharmacy
# pass : 123

# Create your models here.

PAYMENT_CHOICES = (
		("CASH", "CASH"),
		("ONLINE PAY", "ONLINE PAY"),
	)

PAYMENT_STATUS = (
		("FULL PAID", "FULL PAID"),
		("BALANCE", "BALANCE"),
	)

class CustomerMaster(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_mobile = models.CharField(max_length=100)
    payment_mode = models.CharField(verbose_name=" Payments Mode", max_length=100 , choices=PAYMENT_CHOICES)
    payment_bal = models.CharField(verbose_name=" Payments Balance", max_length=100)
    payment_date = models.DateField(null=True)
    created_dt = models.DateTimeField(null=True)


class MedicineMaster(models.Model):
    medicine_name = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=100)
    medicine_unit = models.CharField(max_length=100)
    medicine_exp = models.DateField(null=True)
    medicine_qty = models.CharField(max_length=100)
    medicine_price = models.CharField(max_length=100)
    created_dt = models.DateTimeField(null=True)

class BuyMaster(models.Model):
    fk_customer = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,blank=  True , null= True)
    fk_medicine = models.ForeignKey(MedicineMaster, on_delete=models.CASCADE,blank=  True , null= True)
    discount = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    paid_amt = models.CharField(max_length=100)
    net_total = models.CharField(max_length=100)
    payment_status = models.CharField(verbose_name=" Payments Status", max_length=100 , choices=PAYMENT_STATUS)
    created_dt = models.DateTimeField(null=True)
