#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, days, growth_rate):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm {self.days} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days += 1


rose = Plant("Rose", 30.0, 30, 0.5)
oak = Plant("Oak", 200.0, 365, 1)
cactus = Plant("Cactus", 5.0, 90, 0.05)
sunflower = Plant("Sunflower", 80.0, 45, 2)
fren = Plant("Fern", 15.0, 120, 0.05)
print("=== Garden Plant Registry ===")
print("created: ", end="")
rose.show()
print("created: ", end="")
oak.show()
print("created: ", end="")
cactus.show()
print("created: ", end="")
sunflower.show()
print("created: ", end="")
fren.show()
