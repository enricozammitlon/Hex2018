from buses import *
import json
#At 6:00, each route needs one bus
#Therefore



busses = []		#One of these is spelt wrong... Is it buses or busses??
chargers = []
bus_id = 0

json_file = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[], '10':[], '11':[], '12':[]}
			 


			#Initialise a bus for each route
for route in routes:
	b = busGen(route, 't1', bus_id)
	busses.append(b)
	json_file[str(route['_id'])].append({"_id":str(bus_id), "created_at" : "0", " _type": str(b.bus_type), 'status': True})
	bus_id +=1

maintenance = 0
pay = 0
charging_cost = 0

print(busses)

count  = 10 		#Time in minute - nothing happens in first 10, think of it as turn based where each turn is 10 minutes
	
while count < 4*60:
	for bus in busses:
		if bus.route == None:
			print(bus.bus_type + str(bus.bus_id) + ", unassigned.")
		else:
			print(bus.bus_type + str(bus.bus_id) + ",  R" + str(routes.index(bus.route)+1))
		if not bus.available:
			pay += 10*40/60
			print("Moving...")
			bus.distance_travelled += 10*bus.velocity
			bus.energy -= 10*bus.velocity*1.5
			if bus.distance_travelled >= bus.route['distance']:
				maintenance += 0.3*bus.distance_travelled
				print("Terminates here")
				bus.available = True
				json_file[str(bus.route['_id'])].append({"_id":str(bus.bus_id), "created_at" :str(count) , " _type": str(bus.bus_type), 'status': False})
				bus.newRoute(None)
				bus.distance_travelled = 0
				available_chargers = [i for i in chargers if i.available]
				if not available_chargers:
					chargers.append(B(bus))
		
		if bus.available:
			if bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh
			else:
				for charger in chargers:
					if charger.bus == bus:
						print("Bus charged. Charger vacated.")
						charger.bus = None
						charger.available = True
						bus.battery.cycles -= 1
	for R in routes:

		if count%R['t1']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t1']['frequency']*R['t1']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				b = busGen(R, 't1', bus_id)
				busses.append(b)
				json_file[str(R['_id'])].append({"_id":str(bus_id), "created_at" : str(count), " _type": str(b.bus_type), 'status':True})
				bus_id += 1
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	
	count += 10
	print(len(busses))	

while count >= 4*60 and count < 2*4*60:
	for bus in busses:
		if bus.route == None:
			print(bus.bus_type + str(bus.bus_id)+ ", unassigned.")
		else:
			print(bus.bus_type + str(bus.bus_id) + ",  R" + str(routes.index(bus.route)+1))
		if not bus.available:
			print("Moving...")
			pay += 10*40/60
			bus.distance_travelled += 10*bus.velocity
			bus.energy -= 10*bus.velocity*1.5
			if bus.distance_travelled >= bus.route['distance']:
				print("Terminates here")
				maintenance += 0.3*bus.distance_travelled
				bus.available = True
				json_file[str(bus.route['_id'])].append({"_id":str(bus.bus_id), "created_at" :str(count) , " _type": str(bus.bus_type), 'status': False})
				bus.newRoute(None)
				bus.distance_travelled = 0
				available_chargers = [i for i in chargers if i.available]
				if not available_chargers:
					chargers.append(B(bus))
		
		if bus.available:
			if bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh
			else:

				for charger in chargers:
					if charger.bus == bus:
						print("Bus charged. Charger vacated.")
						charger.bus = None
						charger.available = True
						bus.battery.cycles -= 1

	for R in routes:

		if count%R['t2']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t2']['frequency']*R['t2']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				b = busGen(R, 't1', bus_id)
				busses.append(b)
				json_file[str(R['_id'])].append({"_id":str(bus_id), "created_at" : str(count), " _type": str(b.bus_type), 'status':True})
				bus_id += 1
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	count += 10	
while count >= 2*60 and count < 3*4*60:
	for bus in busses:
		if bus.route == None:
			print(bus.bus_type + str(bus.bus_id) + ", unassigned.")
		else:
			print(bus.bus_type + str(bus.bus_id) + ",  R" + str(routes.index(bus.route)+1))
		if not bus.available:
			print("Moving...")
			pay += 10*40/60
			bus.distance_travelled += 10*bus.velocity
			bus.energy -= 10*bus.velocity*1.5
			if bus.distance_travelled >= bus.route['distance']:
				print("Terminates here")
				maintenance += 0.3*bus.distance_travelled
				bus.available = True
				json_file[str(bus.route['_id'])].append({"_id":str(bus.bus_id), "created_at" :str(count) , " _type": str(bus.bus_type), 'status': False})
				bus.newRoute(None)
				bus.distance_travelled = 0
				available_chargers = [i for i in chargers if i.available]
				if not available_chargers:
					chargers.append(B(bus))
		
		if bus.available:
			if bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh
			else:
				for charger in chargers:
					if charger.bus == bus:
						print("Bus charged. Charger vacated.")
						charger.bus = None
						charger.available = True
						bus.battery.cycles -= 1

	for R in routes:

		if count%R['t3']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t3']['frequency']*R['t3']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				b = busGen(R, 't1', bus_id)
				busses.append(b)
				json_file[str(R['_id'])].append({"_id":str(bus_id), "created_at" : str(count), " _type": str(b.bus_type), 'status':True})
				bus_id += 1
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	count += 10	
while count >= 3*4*60 and count < 4*4*60:
	for bus in busses:
		if bus.route == None:
			print(bus.bus_type +str(bus.bus_id)+ ", unassigned.")
		else:
			print(bus.bus_type + str(bus.bus_id)+ ",  R" + str(routes.index(bus.route)+1))
		if not bus.available:
			print("Moving...")
			pay += 10*40/60
			bus.distance_travelled += 10*bus.velocity
			bus.energy -= 10*bus.velocity*1.5
			if bus.distance_travelled >= bus.route['distance']:
				print("Terminates here")
				maintenance += 0.3*bus.distance_travelled
				bus.available = True
				json_file[str(bus.route['_id'])].append({"_id":str(bus.bus_id), "created_at" :str(count) , " _type": str(bus.bus_type), 'status': False})
				bus.newRoute(None)
				bus.distance_travelled = 0
				available_chargers = [i for i in chargers if i.available]
				if not available_chargers:
					chargers.append(B(bus))
		
		if bus.available:
			if bus.energy <= bus.energy_max:
				print("Charging...")
				bus.energy += 250/6			#Assuming enough Type B chargers for all busses at the station, adds 250/6 kWh
			else:
				for charger in chargers:
					if charger.bus == bus:
						print("Bus charged. Charger vacated.")
						charger.bus = None
						charger.available = True
						bus.battery.cycles -= 1

	for R in routes:

		if count%R['t4']['frequency'] == 0:
	
			available_busses = [x for x in busses if x.available and x.people >= R['t4']['frequency']*R['t4']['passengers']/(4*60) and x.energy >= 1.5* R['distance']]
			print([b.bus_type for b in available_busses])
			if not available_busses:
				print("Creating new bus")
				b = busGen(R, 't1', bus_id)
				busses.append(b)
				json_file[str(R['_id'])].append({"_id":str(bus_id), "created_at" : str(count), " _type": str(b.bus_type), 'status':True})
				bus_id += 1
			else:
				print("Reassigning old bus")
				min(available_busses, key = lambda y: y.people).newRoute(R)

	count += 10	


print(len(busses))
print("Bus cost = " + str( sum([z.price() for z in busses])))
print("Maintenance cost = " + str(maintenance))
print("Pay cost = " + str(pay))
print("Charger cost = " + str(sum([w.price for w in chargers])))
print("Mean cycles remaining = " + str(sum([c.battery.cycles for c in busses])/len(busses)))
with open("f.json",'w') as f:
	json.dump(json_file, f)
