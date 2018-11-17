from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField(required=True,max_length=100, help_text='100 characters max')
	comment = forms.CharField(required=True, widget=forms.Textarea)