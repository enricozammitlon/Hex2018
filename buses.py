#Definitions of classes for buses, battery and route information.
#Not to be executed, rather import

if __name__ == '__main__':
	print("Why are you doing this?")

#Constants
#Efficiency of the motor is assumed to be 1.5 kWh/km
	
maintanance = 0.3 #EUR/km

charging_energy = 0.1 #EUR/kW

eff = 1.5 #kWh/km

driver = 40 #EUR/h

passenger_weight = 73 #kg

max_battery = 400 #kWh

#Chargers
class A:
	power = 30 #kW
	price = 30000 #EUR
	charge_type = 'slow'
	max_charge_I = 60 #A
class B:
	power = 250 #kW
	price = 155000 #EUR
	charge_type = 'medium'
	max_charge_I = 450 #A
class C:
	power = 450 #kW
	price = 260000 #EUR
	charge_type = 'fast'
	max_charge_I = 900 #A


#Buses
class bus:
	available = False
	distance_travelled = 0
	energy_used = 0
	def __init__(self, battery, route):
		self.battery = battery
		self.route = route.copy()
		self.energy = battery.energy_rho * battery.weight
		self.velocity = route['distance']/route['duration']		#in km/min
	def newRoute(self, route):
		self.route = route.copy()
		self.velocity = route['distance']/route['duration']		#In km/min

class LE(bus):
	def price(self):
		return  350000 + self.battery.price #EUR
	bus_type = 'LE'
	length = 9950 #mm
	max_weight = 14870 #kg
	unladen_weight = 7930 #kg
	def weight(self):
		people_weight =  self.max_weight - self.unladen_weight - self.battery.weight
		self.people = people_weight/passenger_weight
		return people_weight
class LF(bus):
	def price(self):
		return  390000 + self.battery.price #EUR
	bus_type = 'LF'
	length = 12000 #mm
	max_weight = 19500 #kg
	unladen_weight = 10645 #kg
#	def weight(self):
#	return self.max_weight - self.unladen_weight - self.battery.weight
	def weight(self):
		people_weight =  self.max_weight - self.unladen_weight - self.battery.weight
		self.people = people_weight/passenger_weight
		return people_weight

class LFA(bus):
	def price(self):
		return  570000 + self.battery.price #EUR
	bus_type = 'LFA'
	length = 18750 #mm
	max_weight  = 29000 #kg
	unladen_weight = 16125 #kg
#	def weight(self):
#      		return self.max_weight - self.unladen_weight - self.battery.weight
	def weight(self):
		people_weight =  self.max_weight - self.unladen_weight - self.battery.weight
		self.people = people_weight/passenger_weight
		return people_weight



def busGen(route, time):

	busWeights = [
		LE(MP(route['distance']), route),
		LF(MP(route['distance']), route),
		LFA(MP(route['distance']), route),
		LE(HP(route['distance']), route),
		LF(HP(route['distance']), route),
		LFA(HP(route['distance']), route)
	]

	return min([x for x in busWeights if x.weight() >= passenger_weight * route[time]['passengers'] * route[time]['frequency']/(4*60)], key=lambda y: y.price())

		

#Batteries
class MP:
	energy_cost = 720  #EUR/kWh
	energy_rho = 70 #Wh/kg
	voltage = 600 #V
	max_charge_I = 450 #A
	max_discharge_I = 450 #A
	charge_type = 'slow'
	cycles = 3000
	def __init__(self, distance):
		self.weight = 1.5*1000*distance/self.energy_rho
		self.price = 1.5*distance*self.energy_cost
class HP:
	energy_cost = 1150 #EUR/kWh
	energy_rho = 60 #Wh/kg
	voltage = 600 #V
	max_charge_I = 635 #A
	max_discharge_I = 500 #A
	charge_type = 'fast'
	cycles = 6500
	def __init__(self, distance):
		self.weight = 1.5*1000*distance/self.energy_rho
		self.price = 1.5*distance*self.energy_cost

#Routes
#Setup in JSON-style dictionary array format
		#km	  #min			  #min	                   #min                    #min                    #min       #m         #s
def makeRoute(distance, duration, t1_passengers, t1_freq, t2_passengers, t2_freq, t3_passengers, t3_freq, t4_passengers, t4_freq, stop_freq, stop_duration):
	routeDict   =  {'distance':distance,
			'duration':duration,
			't1':
				{'passengers':t1_passengers,
				 'frequency': t1_freq},
			't2':
				{'passengers':t2_passengers,
				 'frequency': t2_freq},
			't3':
				{'passengers':t3_passengers,
				 'frequency': t3_freq},
			't4':
				{'passengers':t4_passengers,
				 'frequency': t4_freq},
			'stop_freq':stop_freq,
			'stop_duration':stop_duration}

	return routeDict


R1 = makeRoute(20, 60, 700, 10, 700, 10, 700, 10, 700, 10, 10000, 8*60)
R2 = makeRoute(10, 40, 2000, 10, 300, 20, 2000, 10, 300, 20, 300, 10)
R3 = makeRoute(15, 55, 2000, 10, 300, 20, 2000, 10, 300, 20, 500, 10)
R4 = makeRoute(7, 20, 300, 20, 200, 30, 300, 20, 200, 30, 700, 10)
R5 = makeRoute(6, 20, 2000, 10, 300, 10, 2000, 10, 300, 10, 300, 10)
R6 = makeRoute(20, 60, 1500, 10, 200, 20, 1500, 10, 200, 20, 1000, 20)
R7 = makeRoute(10, 40, 3300, 10, 1000, 10, 3300, 10, 1000, 10, 500, 10)
R8 = makeRoute(25, 70, 1600, 20, 800, 20, 1600, 20, 800, 20, 1000, 20)
R9 = makeRoute(35, 60, 600, 30, 200, 30, 600, 30, 200, 30, 2000, 20)
R10= makeRoute(30, 60, 1000, 30, 600, 30, 1000, 30, 600, 30, 3000, 20)
R11= makeRoute(40, 70, 400, 30, 100, 60, 400, 30, 100, 60, 3000, 20)
R12= makeRoute(35, 60, 1000, 30, 200, 60, 1000, 60, 200, 30, 2000, 20)

routes = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12]
