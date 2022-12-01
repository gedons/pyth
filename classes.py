# Create a class called point
class Point():
	def __init__(self, input1,input2):
		self.x = input1
		self.y = input2

# create an object of the class Point
p = Point(2,8)
print(p.x)
print(p.y)



class Flight():
	def __init__(self, capacity):
		self.capacity = capacity
		#create a lists
		self.passengers = []

	def add_passenger(self, name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passengers)


# create an object of the class Flight
flight = Flight(1)

people = ["harry","Jerry", "Ron"]
for person in people:
	success = flight.add_passenger(person)
	if success:
		print(f"added {person} to flight successfully")
	else:
		print(f"no available seats for {person}")
	


		
		