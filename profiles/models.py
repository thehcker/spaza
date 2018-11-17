from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=150, blank=True, default="Enter your Products description")

	def __unicode__(self):
		return self.name
