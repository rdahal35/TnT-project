from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserSignupView, UserLoginView, SocialSignupView, logout_view, GuestSignupView, HostSignupView
from .models import User

urlpatterns = [
    #needs django social urls
    path('signup/', UserSignupView.as_view(), name='signup' ),
    path('login/', UserLoginView.as_view(), name='user-login' ),
    path('logout/', logout_view, name='logout' ),
    path('social-signup/', SocialSignupView.as_view(), name='social-signup'),
    path('signup/host/', login_required(HostSignupView.as_view()), name='host-signup'),
    path('signup/guest/', login_required(GuestSignupView.as_view()), name='guest-signup'),
    path('rewards/learn/', TemplateView.as_view(template_name='learn-more.html'), name='rewards-learn'),

    #forgot password reset password urls

    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]
