from django.db import models

# Create your models here.

class Event(models.Model):
	id= models.CharField(primary_key=True, max_length=100)
	title= models.CharField(max_length=400)
	start_date= models.CharField(max_length=100)
	end_date= models.CharField(max_length=100)
	color= models.CharField(max_length=100)

	def __str__(self):
		return self.title

class DayDetail(models.Model):
	detail_id= models.CharField(max_length=100, blank=True, null=True)
	date= models.CharField(max_length=20)
	price= models.CharField(max_length=10)
	points= models.CharField(max_length=10)

	def __str__(self):
		return self.date

