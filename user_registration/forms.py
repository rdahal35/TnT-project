from .models import User, GuestProfile, HostProfile
from django import forms

class UserSignupForm(forms.ModelForm):

	password= forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget = forms.PasswordInput)
	
	class Meta:
		model = User	
		fields = ["email"]
	
	def clean(self):
		cleaned_data = super(UserSignupForm, self).clean()

		password1 = cleaned_data.get("password")
		password2 = cleaned_data.get("confirm_password")

		if password1 and password2 and password1 != password2:
			self.add_error('confirm_password', "Password does not match")
		
		return cleaned_data


class GuestSignupForm(forms.ModelForm):

	CHOICES = [
	('Airbnb','Airbnb'),
	('Booking.com','Booking.com'),
	('HomeAway', 'HomeAway'),
	('VRBO', 'VRBO'),
	('Other', 'Other'),
	]

	platform = forms.ChoiceField(choices=CHOICES)

	class Meta:

		model = GuestProfile
		fields = ["name", "phone_number", "address", "email", "platform" ]


class HostSignupForm(forms.ModelForm):
	
	CHOICES=[('I','Individual'),('O','Company/Organization')]
	user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

	class Meta:

		model = HostProfile
		fields = ["name", "phone_number", "user_type", "email" ]


class UserLoginForm(forms.Form):

	email = forms.CharField(label="email_address", max_length=30)
	password = forms.CharField(label="Password", widget= forms.PasswordInput)


class SocialSignupForm(forms.Form):

	CHOICES =[
	('I', 'Individual'),
	('O', 'Organization')
	]

	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget= forms.PasswordInput)

	user_type = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect())

	def clean(self):
		cleaned_data = super(SocialSignupForm, self).clean()

		password1 = cleaned_data.get("password")
		password2 = cleaned_data.get("confirm_password")

		if password1 and password2 and password1 != password2:
			self.add_error('confirm_password', "Password does not match")
		
		return cleaned_data


class ForgotPassword(forms.Form):
	email = forms.CharField(label="email_address", max_length=30)
	