"""
Django settings for TripTnT project.

Author: Sajeet Pokharel

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yhs!pbp902$zt#7rt@z#hucs&y)5!_l+t-gw2khkys9=w)5pye'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #third party packages
    'widget_tweaks',
    'social_django',

    #apps
    'user_registration',
    'host',
    'events',
    'mycalendar',
]

# mail sever to be used in development only (use different email service during production)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'triptnt7156@gmail.com'
EMAIL_HOST_PASSWORD = 'trippassport7156'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'TripTnT Team <noreply@TripTnT.com>'
# ACCOUNT_EMAIL_VERIFICATION = "none"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = "nitesh.ghimire@gmail.com"
# EMAIL_HOST_PASSWORD = "xxxxxxxxx"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
#to use production quality mail server use SendGrid or mail service like that
#see documentation https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html

# This is required because we have extended the user model 
AUTH_USER_MODEL = 'user_registration.User'

#for social login 
AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',
 'social_core.backends.google.GoogleOpenId',
 'social_core.backends.google.GoogleOAuth2',
 'social_core.backends.twitter.TwitterOAuth',
 #'CustomFacebookOauth',
'social_core.backends.facebook.FacebookOAuth2',
 'social_core.backends.linkedin.LinkedinOAuth2',
 #'social.backends.linkedin.LinkedinOAuth2'
 # #'social_core.backends.linkedin.LinkedinOAuth2'

 'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'


#user auth models
SOCIAL_AUTH_USER_MODEL = 'user_registration.User'

'''
#Used to define the max length of the field uid. A value of 223 should work when using MySQL InnoDB which impose a 767 bytes limit (assuming UTF-8 encoding).
SOCIAL_AUTH_UID_LENGTH = <int>

#Nonce model has a unique constraint over ('server_url', 'timestamp', 'salt'), 
#salt has a max length of 40, so server_url length must be tweaked using this setting.
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = <int>

#Association model has a unique constraint over ('server_url', 'handle'), both fields lengths
#can be tweaked by these settings.
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = <int> or SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = <int>
'''
#This controls the length of the UUID appended to usernames.
SOCIAL_AUTH_UUID_LENGTH = 16

#If you want to use the full email address as the username, define this setting.
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

#For those that prefer slugged usernames, the get_username pipeline can apply a slug transformation 
#(code borrowed from Django project) by defining this setting to True.
SOCIAL_AUTH_SLUGIFY_USERNAMES = False

#By default a set of regular expressions are applied over usernames to clean them from usual undesired
#characters like spaces. Set this setting to False to disable this behavior.
SOCIAL_AUTH_CLEAN_USERNAMES = True
'''
for extra arguments
SOCIAL_AUTH_<uppercase backend name>_AUTH_EXTRA_ARGUMENTS = {...}
'''

'''
refer to https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html for documentation on 
some missed settings


'''

LOGIN_URL="/login/"

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

#homepage redirect after login
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

#if login fail then redirect to login with errors
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/'

#Is used as a fallback for LOGIN_ERROR_URL
SOCIAL_AUTH_LOGIN_URL = '/login/'

#For new users redirect to signup Note that ?next=/foo is appended if present, if you want new users to go to next, you’ll need to do it yourself.
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/social-signup/'

# Like SOCIAL_AUTH_NEW_USER_REDIRECT_URL but for new associated accounts (user is already logged in). Used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/'

#after connect The user will be redirected to this URL when a social account is disconnected
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/logout-social/'

#Inactive users can be redirected to this URL when trying to authenticate.
SOCIAL_AUTH_INACTIVE_USER_URL = '/login/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #middleware for django social auth
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'TripTnT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                #for django schedule
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'TripTnT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# # #also need to define a sesssion engine for cache data
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'


# #to store user data in caches for dynamic performance
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
#Bower requirements


STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join( BASE_DIR, 'static'), 
#'/var/www/static/',
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '159050544860-bdtkdt02hus7sckm71nandobo4tficj3.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '3pY4n1IwqrdDIRA-OjrtmaYg'
SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_FACEBOOK_KEY = '298985213991345'
SOCIAL_AUTH_FACEBOOK_SECRET = '7654dfc5ecaa54172a0f6cfbe5ddfdbc'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['public_profile', 'email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'first_name,last_name,gender,picture,link'}

SOCIAL_AUTH_TWITTER_KEY = 'WfIPFK65nqDWRh4Szq3oIitZ5'
SOCIAL_AUTH_TWITTER_SECRET = 'LvNT62Pk5gOYXy2Ob3Oh2m98QxS72hhDbm0GwzlWULRd302JKm'


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '81lvl3ah7igqz4'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '9hZDpunCjwxSTZNQ'
SOCIAL_AUTH_LINKEDIN_SCOPE = [ 'r_basicprofile' ]

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

