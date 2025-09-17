# Hierarchical Inheritance Example: Vehicle as base class

class Vehicle:
	def show(self):
		print("This is a vehicle.")

class Bike(Vehicle):
	def bike_info(self):
		print("This is a bike.")

class Car(Vehicle):
	def car_info(self):
		print("This is a car.")

class Bus(Vehicle):
	def bus_info(self):
		print("This is a bus.")

class Truck(Vehicle):
	def truck_info(self):
		print("This is a truck.")

# Example usage
b = Bike()
c = Car()
bu = Bus()
t = Truck()

b.show()
b.bike_info()

c.show()
c.car_info()

bu.show()
bu.bus_info()

t.show()
t.truck_info()
