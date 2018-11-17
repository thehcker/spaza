from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	#print(request.session.get('first_name','Unknown')) #Getter
	context = locals()
	template = 'index.html'
	return render(request,template,context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)
@login_required
def userProfile(request):
	title = 'My Profile'
	form = request.user
	context = {'title':title,'form':form,}
	template = 'profile.html'
	return render(request,template,context)

def faq(request):
	context = locals()
	template = 'faq.html'
	return render(request,template,context)
