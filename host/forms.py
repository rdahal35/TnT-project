from django import forms
from .models import Listing


class AddUrlForm(forms.Form):

	platform = forms.CharField(max_length=200)
	url = forms.URLField(max_length=200, min_length=1)

class AddListingForm(forms.ModelForm):
	PLATFORM_CHOICES = [
	('Airbnb','Airbnb'),
	('Booking.com', 'Booking.com'),
	('HomeAway', 'HomeAway'),
	('VRBO', 'VRBO'),
	('Other', 'Other'),
	]

	platform = forms.ChoiceField(choices= PLATFORM_CHOICES) 

	class Meta:

		model = Listing

		fields = [
		'title',
		'platform',
		'platform_link',
		'ical_link',
		'address',
		'bed_room',
		'beds',
		'guests',
		'house_rules',
		'cover_image',
		'bath',
		'price_per_night',
		'availability',
		'cancellations'
		]

class AddNightlyPoints(forms.Form):
	listing = forms.CharField()
	average_nightly_points = forms.IntegerField()
	points_per_dollar_spent = forms.IntegerField()
	average_points_per_night = forms.IntegerField()

