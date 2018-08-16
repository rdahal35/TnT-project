from django.urls import path, include
from . import views

urlpatterns = [
    path('event-calendar/', views.CalendarDownload, name='event-calendar'),
]