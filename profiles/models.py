from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
	name = models.CharField(max_length=100,blank=True)
	address = models.CharField(max_length=150, blank=True)
	city = models.CharField(max_length=120,default='')
	phone = models.IntegerField(default=0)
	last_seen = models.DateTimeField(auto_now=True)
	description = models.TextField(max_length=150, blank=True, default="Enter your Products description")
	image = models.ImageField(upload_to='documents/',null=True,blank=True)

	def __unicode__(self):
		return self.user.username
# @receiver(post_save,sender=User)
# def create_profile(sender,instance,created,**kwargs):
# 	if created:
# 		profile,new = Profile.objects.get_or_create(user=instance)

# 	post_save.connect(create_profile,sender=User)

# def create_profile(sender,**kwargs):
# 	if kwargs['created']:
# 		profile = Profile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile,sender=User)
def create_profile(sender,instance,**kwargs):
	userprofile,new = Profile.objects.get_or_create(user=instance)
 
post_save.connect(create_profile,sender=User)

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.ImageField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#     	return self.description

class GuestEmail(models.Model):
	email = models.EmailField()
	active = models.BooleanField(default=True)
	update = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email