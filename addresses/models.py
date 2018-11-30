from django.db import models
from billing.models import BillingProfile

ADDRESS_TYPES = (
		('billing','billing'),
		('shipping','shipping'),
	)

# Create your models here.

class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
	address_type = models.CharField(max_length=120,choices=ADDRESS_TYPES)
	address_line1 = models.CharField(max_length=120)
	address_line2 = models.CharField(max_length=120,null=True,blank=True)
	city = models.CharField(max_length=120)
	country = models.CharField(max_length=120,default="Kenya")
	province = models.CharField(max_length=120,default="Coast")
	postal_code = models.CharField(max_length=120)

	def __str__(self):
		return str(self.billing_profile)

	def get_address(self):
		return "{line1}\n{line2}\n{city}\n{province}-{postal}\n{country}".format(
				line1 = self.address_line1,
				line2 = self.address_line2 or "",
				city = self.city,
				province = self.province,
				postal = self.postal_code,
				country = self.country

			)

