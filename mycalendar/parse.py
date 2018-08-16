from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

def parse(filename):
	events=[]
	g = open(filename,'rb')
	gcal = Calendar.from_ical(g.read())
	for component in gcal.walk():
	    if component.name == 'VEVENT':
	    	events.append(component)
	        # print(component.get('summary'))
	        # print(component.get('dtstart'))
	        # print(component.get('dtend'))
	        # print(component.get('dtstamp'))
	g.close()
	return events
#print(events)

#for event in events:
 #   print('This is a event')
  #  print(event['SUMMARY'])