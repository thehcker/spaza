from django.contrib import admin
from profiles.models import Profile
from products.models import Product

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile,ProfileAdmin)
#admin.site.register(Product)