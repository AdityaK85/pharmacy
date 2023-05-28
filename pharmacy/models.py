from django.db import models
# user : pharmacy
# pass : 123

# Create your models here.

PAYMENT_CHOICES = (
		("CASH", "CASH"),
		("ONLINE PAY", "ONLINE PAY"),
	)

class CustomerMaster(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_mobile = models.CharField(max_length=100)
    payment_mode = models.CharField(verbose_name=" Payments Mode", max_length=100 , choices=PAYMENT_CHOICES)
    payment_bal = models.CharField(verbose_name=" Payments Balance", max_length=100)
