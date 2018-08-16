from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.http import Http404, JsonResponse, HttpResponseRedirect, HttpResponse

from user_registration.models import User
from .forms import AddUrlForm, AddListingForm
from .models import Listing
from .scraper import url_scrapper
from .selenum import UrlScrapper

class AddUrlView(View):

	form_class = AddUrlForm
	template_name = 'add_listing_url.html'

	def get(self, request):

		if not request.user.is_authenticated:
			raise Http404

		listings= Listing.objects.filter(user=request.user)
		form = self.form_class(None)
		context_dict={
		'username':request.user.username,
		'listings': listings,
		'form': form,
		}
		return render(request, self.template_name, context_dict)

	def post(self, request):

		form = self.form_class(request.POST)

		if form.is_valid():

			url = form.cleaned_data['url']
			scraper = UrlScrapper()	
			new_results = scraper.scrape_property(url)
			
			# results = url_scrapper(url)

			context_dict = {
			# 'results': results,
			'form': form,
			'new_results':new_results
			}
			# request.session['results'] = results
			request.session['new_results'] = new_results
			return redirect('/host/add-listing/')

		return render(request, self.template_name, {'form':form})

class AddListingView(View):

	form_class = AddListingForm
	template_name = 'add_listing.html'

	def get(self, request):
		if not request.user.is_authenticated:
			raise Http404

		# results = request.session['results']
		try:
			new_results = request.session['new_results']
		except:
			new_results = None
		
		form = self.form_class(None)
		context_dict={
		'username':request.user.username,
		'form': form,
		# 'results':results,
		'results': new_results
		}

		return render(request, self.template_name, context_dict)

	def post(self, request):

		form = self.form_class(request.POST, request.FILES)

		if form.is_valid():
			try:
				new_results = request.session['new_results']
			except:
				new_results = None

			listing = form.save(commit=False)
			listing.user = request.user
			listing.username = request.user.username

			if not listing.cover_image and 'image_name' in new_results:
				listing.cover_image = new_results['image_name']

			listing.save()
			request.session['new_results'] = dict()
			return redirect('/host/dashboard/')

		return render(request, self.template_name, {'form':form})


class AddNightlyPoints(View):

	template_name = "host-signup-2.html"

	def get(self, request):

		if not request.user.is_authenticated:
			raise Http404

		listings = Listing.objects.filter(username__iexact=request.user.username)
		
		context_dict = {
		
		'listings':listings,

		}
		return render(request, self.template_name, context_dict)

		


class HostDashboardView(View):

	template_name = 'dashboard/host_dashboard.html'
	form_class = AddListingForm

	def get(self, request):

		if not request.user.is_authenticated:
			return redirect('/login/')

		#for getting the title of listing in listing edit view modal	
		if 'action' in request.GET:
			listing_title = request.GET['listing_name']
			listing_data = Listing.objects.get(title__iexact = listing_title, username__iexact = request.user.username )

			if request.GET['action']=="view" :
				print("hello")
				return HttpResponse(listing_data.id)
			
			else:
				form = self.form_class(instance = listing_data)
			

				context_dict = {

				'results':listing_data,
				'form':form,
				}
			
				return render(request, 'addlistingform.html', context_dict)

			
		listings= Listing.objects.filter(user=request.user)
		context_dict={
		'username':request.user.username,
		'listings': listings,
		}
		return render(request, self.template_name, context_dict)

	def post(self, request):
		
		listing_title = request.POST['title']
		listing_data = Listing.objects.get(title__iexact = listing_title, username__iexact = request.user.username )

		form = self.form_class(request.POST or None, request.FILES or None, instance=listing_data)
		
		if form.is_valid():

			edited_listing = form.save()

			return redirect('/host/dashboard/')

		context_dict = {

			'results':listing_data,
			'form':form,
		}

		return render(request, 'addlistingform.html', context_dict)




class ListingDeleteView(HostDashboardView):

	def post(self, request):

		listing_title = request.POST['listing_name']
		Listing.objects.filter(title__iexact= listing_title).delete()
		
		listings= Listing.objects.filter(user=request.user)
		context_dict={
		'username': request.user.username,
		'listings': listings,

		}
		return render(request, self.template_name, context_dict )


class HostListingView(View):

	template_name = "view_listing.html"
	
	def get(self, request, id):
		
		listing_data= Listing.objects.get(id=id)

		context_dict = {
		'results':listing_data,
		}
		
		return render(request, self.template_name, context_dict)



