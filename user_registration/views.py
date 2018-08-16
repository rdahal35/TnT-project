from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse

from .forms import UserSignupForm, GuestSignupForm, HostSignupForm, UserLoginForm, SocialSignupForm, ForgotPassword
from .models import User, HostProfile

def logout_view(request):

	logout(request)
	return redirect('/')

class UserSignupView(View):

		form_class = UserSignupForm
		template_name = 'registration/signup.html'

		def get(self, request):

			form = self.form_class(None)
			return render(request, self.template_name,{'form':form})

		def post(self, request):

			form = self.form_class(request.POST)

			if form.is_valid():

				user = form.save(commit = False)

				user_email = form.cleaned_data['email']
				password = form.cleaned_data['password']
				confirm_password = form.cleaned_data['confirm_password']

				user.set_password(password)
				user.save()
				user = authenticate(email=user_email, password=password)

				if user is not None:

					#to check if disabled or banned status

					if user.is_active:

						login(request, user)
						return redirect('/')

			return render(request, self.template_name, {'form':form})


class UserLoginView(View):


	form_class = UserLoginForm
	template_name = 'registration/login.html'

	def get(self, request):

		form = self.form_class(None)
		return render(request, self.template_name,{'form':form})

	def post(self, request):

		form = self.form_class(request.POST)

		if form.is_valid():
			
			user_email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(email=user_email, password=password)

			if user is not None:

				#to check if disabled or banned status
				if user.is_active:
					login(request, user)
					return redirect('/')
			else:

				messages.error(request,'Login Failed! Please Try Again...')
				return render(request, self.template_name, {'form':form})



		return render(request, self.template_name, {'form':form})


class SocialSignupView(View):
	
	form_class = SocialSignupForm
	template_name = 'social-signup.html'

	def get(self, request):
		request.session['user_email']= request.user.email

		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):

		form = self.form_class(request.POST)

		if form.is_valid():

			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			user_type = form.cleaned_data['user_type']
			user_email = request.session['user_email']
			userdata = User.objects.get(email__exact= user_email)
			userdata.set_password(password)
			userdata.user_type = user_type
			userdata.save()

			user = authenticate(email=userdata.email, password= password)

			if user is not None:

				if user.is_active:

					login(request,user)
					return redirect('/')
			else:
				messages.error(request,'Setup Failed! Please Try Again...')
				return render(request, self.template_name, {'form':form})

		return render(request, self.template_name, {'form':form})	


class HostSignupView(View):

	form_class = HostSignupForm
	template_name = 'signup_host.html'

	def get(self, request):

		form = self.form_class(None)
		context_dict={
		'user': request.user,
		'form': form
		}
		try:
			is_host= HostProfile.objects.get(user=request.user)
			return redirect('/host/dashboard/')
		except HostProfile.DoesNotExist:
			return render(request, self.template_name,context_dict)

	def post(self, request):

		form = self.form_class(request.POST)
		
		if form.is_valid():

			host = form.save(commit = False)
			host.user = request.user
			#remove the duplicate user
			
			host.save()	
			
			return redirect('/host/add-listing/')

		return render(request, self.template_name, {'form':form})


class GuestSignupView(View):

	form_class = GuestSignupForm
	template_name = 'signup_guest.html'

	def get(self, request):

		form = self.form_class(None)
		context_dict={
		'user': request.user,
		'form':form
		}
		return render(request, self.template_name,context_dict)

	def post(self, request):

		form = self.form_class(request.POST)
		if form.is_valid():

			guest = form.save(commit = False)
			guest.user = request.user
			#remove the duplicate user
			
			guest.save()	
			
			return redirect('/')

		return render(request, self.template_name, {'form':form})
		







