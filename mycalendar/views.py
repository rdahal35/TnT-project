from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Event, DayDetail
from django.http import HttpResponse
import simplejson as json
from django.http import JsonResponse
from django.views.generic import TemplateView

from .parse import parse
import requests

# Create your views here.


class SearchCalendar(TemplateView):
	template_name= 'mycalendar/home.html'

class HostSignUp(TemplateView):
	template_name= 'host-signup-2.html'
	# template_name= "mycalendar/themcalendar.html"

@csrf_exempt
def CalendarView(request):

	eve= []
	if request.method== 'POST':
		url= request.POST.get('url')

		try:
			r= requests.get(url, allow_redirects=True)
			open('mycal.ics', 'wb').write(r.content)
			ical_events= parse('mycal.ics')

		except Exception as e:
			ical_events=[]
		
	else:
		ical_events= parse('mycal.ics') 

	for event in ical_events:
		event_sub= {}

		event_sub['title']= str(event.get('summary'))
		event_sub['start']= str(event.get('dtstart').dt)
		event_sub['end']=  str(event.get('dtend').dt)
		eve.append(event_sub)
	
	events_data = json.dumps(eve)

	events= Event.objects.all()	
	return render(request, 'calendar.html', {'events': events, 'ical_events': eve})


def PriceCalendar(request):
	details= DayDetail.objects.all()
	return render(request, 'mycalendar/price_calendar.html', { 'details': details })

def saveEvent(request):
	if request.is_ajax():
		message= "Yes I am here"
		eventData = request.GET.get('eventData', None)
		data = json.loads(eventData)
		Event.objects.create(title=data['title'], start_date=data['start'], end_date= data['end'], color=data['color'])
	else:
		message= " Not ajax"
	return JsonResponse(data)

@csrf_exempt
def saveDayDetail(request):
	# print("hello there")
	if request.is_ajax():
		message=" happy "
		detail_json= request.GET.get('details', None)
		# print(detail_json)
		
		details= json.loads(detail_json)
		for detail in details:
			try:
				det= DayDetail.objects.get(date=detail['date'])
				det.price= detail['price']
				det.points= detail['point']
				det.save()
			except DayDetail.DoesNotExist:
				DayDetail.objects.create(
						detail_id=detail['id'], 
						date=detail['date'], 
						price=detail['price'], 
						points=detail['point']
					)
		
	else: 
		message=" Not ajax "
	return JsonResponse(message, safe=False)
	
@csrf_exempt
def editDayDetail(request):
	if request.is_ajax():
		message=" happy "
		detail_json= request.GET.get('details', None)
		# print(detail_json)
		
		detail= json.loads(detail_json)
		try:
			det= DayDetail.objects.get(date=detail['date'])
			det.price= detail['price']
			det.points= detail['point']
			det.save()
		except DayDetail.DoesNotExist:
			DayDetail.objects.create(
					detail_id=detail['id'], 
					date=detail['date'], 
					price=detail['price'], 
					points=detail['point']
				)
		
	else: 
		message=" Not ajax "
	return JsonResponse(message, safe=False)
	

