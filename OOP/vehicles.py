class Vehicle:
    def move(self):
        print("This vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the skies ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the ocean 🚢")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the pathway 🚴")

class Train(Vehicle):
    def move(self):
        print("Running on railway tracks 🚆")


# Creating instances of vehicles
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()
train = Train()

# Calling the move() method
car.move()      # 🚗 Driving on the road
plane.move()    # ✈️ Flying through the skies
boat.move()     # 🚢 Sailing across the ocean
bicycle.move()  # 🚴 Pedaling on the pathway
train.move()    # 🚆 Running on railway tracks