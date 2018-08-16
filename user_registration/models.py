from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings

class UserManager(BaseUserManager):

	def _create_user(self, username, email, password, **extra_fields):
		if not email:
			raise ValueError('User must have email address')

		email = self.normalize_email(email)
		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		_('username'),
		max_length=150,
		blank=True,
		help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		error_messages={
			'unique': _("A user with that username already exists."),
		},
	)
	email = models.EmailField(_('email address'), unique=True, null=True)

	newsletter = models.BooleanField(
		default=False
	)
	description = models.TextField(blank=True, null=True)
	dob = models.DateField(blank=True, null=True)
	
	

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
	)

	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. '
			'Unselect this instead of deleting accounts.'
		),
	)

	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, auto_now=False)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


class Address(models.Model):

	country = models.CharField(max_length=50, null=True, blank=True)
	street_address = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	zip_postal_code = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return ('{}{}'.format(self.city,self.country))

class HostProfile(models.Model):

	user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	name = models.CharField(max_length=50, null=True, blank=True)
	phone_number = models.CharField(max_length=20, null=True, blank=True)
	email = models.EmailField(unique=True, null=True)
	USER_TYPE_CHOICES=[('I','Individual'),
	('O','Company/Organization')]

	user_type = models.CharField(max_length=1, choices= USER_TYPE_CHOICES, null=True, blank=True)
	


class CoHostProfile(User):

	pass

class GuestProfile(models.Model):

	user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(unique=True, null=True)
	phone_number = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=50, null=True, blank=True)
	PLATFORM_CHOICES = [
	('Airbnb','Airbnb'),
	('Booking.com', 'Booking.com'),
	('HomeAway', 'HomeAway'),
	('VRBO', 'VRBO'),
	('Other', 'Other'),
	]

	platform = models.CharField(max_length=20, choices= PLATFORM_CHOICES, null=True, blank=True)


class TaskerProfile(User):

	pass

class TaskMasterProfile(User):

	pass


