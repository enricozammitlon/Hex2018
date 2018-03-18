from buses import *
import sys

#At 6:00, each route needs one bus
#Therefore

busses = []		#One of these is spelt wrong... Is it buses or busses??


count  = 0 		#Time in minutes
			#Initialise a bus for each route
for route in routes:
	busses.append(busGen(route, 't1'))
print(busses)

	
while count < 4*60:
	for bus in busses:
		bus.distance_travelled += 10*bus.velocity
		
		bus.energy -= 10*bus.velocity*1.5

		if bus.available:
			bus.distance_travelled = 0

		if bus.distance_travelled >= bus.route['distance']:
			bus.available = True
		
	count+=10

 
