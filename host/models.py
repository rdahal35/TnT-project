from django.db import models
from django.conf import settings


class Listing(models.Model):
    PLATFORM_CHOICES = [
    ('Airbnb','Airbnb'),
    ('Booking.com', 'Booking.com'),
    ('HomeAway', 'HomeAway'),
    ('VRBO', 'VRBO'),
    ('Other', 'Other'),
    ]

    platform = models.CharField(max_length=20, choices= PLATFORM_CHOICES, null=True, blank=True)
    platform_link = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ical_link = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    guests = models.IntegerField(blank=True, null=True)
    bath = models.IntegerField(blank=True, null=True)
    bed_room = models.IntegerField(blank=True, null=True)
    price_per_night = models.IntegerField(blank=True, null=True)
    house_rules = models.TextField(blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
    cancellations = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(blank=True, upload_to='cover_image/', null=True)

    def __str__(self):
    	return "%s ,%s"%(self.title, self.address)