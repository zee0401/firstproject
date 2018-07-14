import datetime
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
	print("Good morning")
elif hour > 17:
	print("Good evening")
else:
	print("Good afternoon")
	
#import date time
