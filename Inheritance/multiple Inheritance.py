# Multiple Inheritance Example: Wheel and Rubber -> Tyre

class Wheel:
	def wheel_info(self):
		print("This is a wheel.")

class Rubber:
	def rubber_info(self):
		print("This is made of rubber.")

class Tyre(Wheel, Rubber):
	def tyre_info(self):
		print("This is a tyre, which has both wheel and rubber properties.")

#example usages
t=Tyre()
t.wheel_info()
t.rubber_info()
t.tyre_info()
