from buses import *

#At 6:00, each route needs one bus
#Therefore

busses = []		#One of these is spelt wrong... Is it buses or busses??


			#Initialise a bus for each route
for route in routes:
	busses.append(busGen(route, 't1'))
print(busses)

count  = 10 		#Time in minute - nothing happens in first 10, think of it as turn based where each turn is 10 minutes
	
while count < 4*60:
	for bus in busses:
		if bus.route == None:
			print(bus.bus_type + ", unassigned.")
		else:
			print(bus.bus_type + ",  R" + str(routes.index(bus.route)+1))
		if not bus.available:
			print("Moving...")
			bus.distance_travelled += 10*bus.velocity
			bus.energy -= 10*bus.velocity*1.5
			if bus.distance_travelled >= bus.route['distance']:
				print("Terminates here")
				bus.available = True
				bus.newRoute(None)
		
		if bus.available:
			print("Charging...")
			bus.distance_travelled = 0
			bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh


	for R in routes:

		if count%R['t1']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t1']['frequency']*R['t1']['passengers']/(4*60) and bus.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if available_busses == []:
				print("Creating new bus")
				busses.append(busGen(R, 't1'))
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	
	count+=10 
print(len(busses))
