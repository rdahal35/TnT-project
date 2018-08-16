from django.shortcuts import render
import requests
from .parse import parse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def CalendarDownload(request):
	if request.method== 'POST':
		url= request.POST.get('url')
		r= requests.get(url, allow_redirects=True)
		open('mycal.ics', 'wb').write(r.content)
		events= parse('mycal.ics')
		eve= []
		for event in events:
			ev= {
				'title': event.get('summary'),
				'dstart': event.get('dtstart').dt,
				'dtend': event.get('dtend').dt,
			}
			eve.append(ev)
		
			# print(event.get('summary'))
		print(eve)
		return render(request, 'events.html', {'events': eve} )
		# {'events': [ event.get('summary') for event in events]}
	else:
		return render(request, 'events.html')