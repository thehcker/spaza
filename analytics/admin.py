from django.contrib import admin
from .models import ObjectViewed, UserSession

# Register your models here.
class ObjectViewedAdmin(admin.ModelAdmin):
	class Meta:
		model = ObjectViewed

admin.site.register(ObjectViewed, ObjectViewedAdmin)
admin.site.register(UserSession)
