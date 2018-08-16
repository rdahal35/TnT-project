from django.contrib import admin
from user_registration.models import User, HostProfile, GuestProfile
# Register your models here.
admin.site.register(User)
admin.site.register(HostProfile)
admin.site.register(GuestProfile)