from django.contrib import admin
from profiles.models import Profile,GuestEmail
from products.models import Product


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile,ProfileAdmin)
admin.site.register(GuestEmail)
#admin.site.register(Product)