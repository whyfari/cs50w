#!/usr/bin/python3.7

class Point():
    # magic method (constructor)
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Flight():
    def __init__(self,cap):
        self.capacity = cap
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():
            print(f"Not enough seats to add {name}")
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)



# don't need to provide the 'self' paramter
p = Point(3,4)
print ("print class p.x:", p.x, "p.y:", p.y)
print ("print class: p :", p, "p.x:", p.x)

flight = Flight(4)
people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if not flight.add_passenger(person):
        print ("No more capacity; not adding any more")
        break
    else:
        print (f"Sucessfully added {person}")

    




