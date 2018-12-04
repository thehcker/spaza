from django import forms
from profiles.models import Profile,GuestEmail


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','address','city','description', 'image' )

class GuestForm(forms.Form):
	# class Meta:
	# 	model = GuestEmail
	# 	fields = 'email'
	email = forms.EmailField()
