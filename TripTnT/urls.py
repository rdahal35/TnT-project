from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from user_registration.views import UserSignupView, UserLoginView, SocialSignupView
from user_registration.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='homeview'),
    #needs django social urls
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('user_registration.urls')),
    path('', include('host.urls')),
    path('', include('events.urls')),
    path('', include('mycalendar.urls')),
 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



