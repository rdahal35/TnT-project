from django.urls import path, include
from django.views.generic import TemplateView
from .views import AddUrlView, AddListingView, AddNightlyPoints, HostDashboardView, ListingDeleteView, HostListingView

urlpatterns = [
    #needs django social urls
    path('host/add-listing-url/', AddUrlView.as_view(), name='add-listing-url' ),
    path('host/add-listing/', AddListingView.as_view(), name='add-listings' ),
    path('host/add-points/', AddNightlyPoints.as_view(), name="add-points"),
    path('host/dashboard/', HostDashboardView.as_view(), name="host-dashboard"),
    path('host/delete/listing/', ListingDeleteView.as_view(), name= "delete-listing"),
    path('host/view/listing/<id>/', HostListingView.as_view(), name= "view-listing"),



   
]
