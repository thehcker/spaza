from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from profiles.forms import ProfileForm,GuestForm
from profiles.models import Profile,GuestEmail
from profiles.forms import GuestForm
from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator
from profiles.models import Profile

#from profiles.models import Profile

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

def faq(request):
	context = locals()
	template = 'faq.html'
	return render(request,template,context)


@login_required
def userProfile(request):
	user = Profile.objects.new_or_get(request)
	title = Profile.objects.all()
	#profile = request.user.profile
	context = {"title":title, "user": user}
	template = 'core/profile.html'
	return render(request,template,context)

def model_profile_upload(request):
	try:
		profile = request.user.profile
	except Profile.DoesNotExist:
		profile = Profile(user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = ProfileForm(instance=profile)
	return render(request, 'model_profile_upload.html', {
        'form': form
    })
	
	
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES)
    #     if form.is_valid():

    #         form.save()
    #         return redirect('profile')
    # else:
    #     form = ProfileForm()
    # return render(request, 'model_profile_upload.html', {
    #     'form': form
    # })
@login_required # account/login/?next=/some/path
def account_home_view(request):
	return render(request, "account/account_home.html", {})


# class LoginRequiredMixin(object):
# 	@method_decorator(login_required)
# 	def dispatch(self, *args, *Kwargs):
# 		return super(LoginRequiredMixin, self).dispatch(self, *args, **kwargs)

#LoginRequiredMixin
class AccountHomeView(LoginRequiredMixin,DetailView):
	template_name = "account/account_home.html"
	def get_object(self):
		return self.request.user

def guest_register_view(request):
	form = GuestForm(request.POST or None)
	template = 'account/snippets/form1.html'
	context = {
		"form":form
	}
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None
	if form.is_valid():
		email = form.cleaned_data.get("email")
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = new_guest_email.id
		email = form.cleaned_data.get("email")
		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)
		else:
			return redirect("carts:checkout")
	return redirect("carts:checkout")
	
