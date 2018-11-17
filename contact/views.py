from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contactForm
from django.conf import settings

# Create your views here.

def contact(request):
	title = 'Contact Us'
	form = contactForm(request.POST or None)
	context = {'title': title, 'form':form,}
	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Email from Isaac'
		message = '%s %s' %(comment,name) 
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]

		send_mail(subject,message,emailFrom,emailTo, fail_silently=False, )
		title = 'Thanks'
		confirm_message = 'Thanks for contacting us. We will get right back to you soon'
		context = {'title': title, 'confirm_message':confirm_message,}
	
	template = 'contact.html'
	return render(request,template,context)
