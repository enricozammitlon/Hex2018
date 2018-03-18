from buses import *

#At 6:00, each route needs one bus
#Therefore

busses = []		#One of these is spelt wrong... Is it buses or busses??


			#Initialise a bus for each route
for route in routes:
	busses.append(busGen(route, 't1'))

maintenance = 0

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
				maintenance += 0.3*bus.distance_travelled
				print("Terminates here")
				bus.available = True
				bus.newRoute(None)
				bus.distance_travelled = 0
		
		if bus.available:
			while bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh


	for R in routes:

		if count%R['t1']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t1']['frequency']*R['t1']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				busses.append(busGen(R, 't1'))
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	
	count += 10
	print(len(busses))	

while count >= 4*60 and count < 2*4*60:
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
				maintenance += 0.3*bus.distance_travelled
				bus.available = True
				bus.newRoute(None)
				bus.distance_travelled = 0
		
		if bus.available:
			while bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh


	for R in routes:

		if count%R['t2']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t2']['frequency']*R['t2']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				busses.append(busGen(R, 't2'))
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	count += 10	
while count >= 2*60 and count < 3*4*60:
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
				maintenance += 0.3*bus.distance_travelled
				bus.available = True
				bus.newRoute(None)
				bus.distance_travelled = 0
		
		if bus.available:
			while bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh


	for R in routes:

		if count%R['t3']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t3']['frequency']*R['t3']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				busses.append(busGen(R, 't3'))
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	count += 10	
while count >= 3*4*60 and count < 4*4*60:
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
				maintenance += 0.3*bus.distance_travelled
				bus.available = True
				bus.newRoute(None)
				bus.distance_travelled = 0
		
		if bus.available:
			while bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh


	for R in routes:

		if count%R['t4']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t4']['frequency']*R['t4']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				busses.append(busGen(R, 't4'))
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	count += 10	


print(len(busses))
print(sum(z.price() for z in busses))
