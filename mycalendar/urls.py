from django.urls import path, include
from . import views

urlpatterns = [
    path('calendar/', views.CalendarView, name='calendar'),
    path('priceCalendar/', views.PriceCalendar, name='price_calendar'),
    path('SearchCalendar/', views.SearchCalendar.as_view(), name='search_calendar'),
    path('SaveEvent/', views.saveEvent, name='event_save'),
    path('SaveDetail/', views.saveDayDetail, name='save_detail'),
    path('EditDetail/', views.editDayDetail, name='edit_detail'),    
]