#Constants
maintanance = 0.3 #EUR/km

charging_energy = 0.1 #EUR/kW

driver = 40 #EUR/h

chargers = {'30':30000, '250':155000, '450':260000} #kW : EUR

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
class LE:
	def __init__(self, battery):
		self.battery = battery
	price = 350000 #EUR
	length = 9950 #mm
	max_weight = 14870 #kg
	weight = 7930 #kg
class LF:
	def __init__(self, battery):
		self.battery = battery
	price = 390000 #EUR
	length = 12000 #mm
	max_weight = 19500 #kg
	weight = 10645 #kg
class LFA:
	def __init__(self, battery):
		self.battery = battery
	price = 570000 #EUR
	length = 18750 #mm
	max_weight  = 29000 #kg
	weight = 16125 #kg

#Batteries
class MP:
	energy_cost = 720  #EUR/kWh
	energy_rho = 70 #Wh/kg
	voltage = 600 #V
	max_charge_I = 450 #A
	max_discharge_I = 450 #A
	charge_type = 'slow'
	cycles = 3000

class HP:
	energy_cost = 1150 #EUR/kWh
	energy_rho = 60 #Wh/kg
	voltage = 600 #V
	max_charge_I = 635 #A
	max_discharge_I = 500 #A
	charge_type = 'fast'
	cycles = 6500
