#!/usr/bin/env python3
class Plant:

    def __init__(self,  name,   height, days,   growth_rate):
        self.name = name
        if (height < 0):
            print(f"{name}: Error, height can't be negative")
            self._height = 0
        else:
            self._height = height
        if (days < 0):
            print(f"{name}: Error, age can't be negative")
            self._days = 0
        else:
            self._days = days
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm {self._days} days old")

    def grow(self):
        self._height += self.growth_rate

    def age(self):
        self._days += 1

    def set_height(self, value):
        if (value < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def set_age(self, value):
        if (value < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = value
            print(f"Age updated: {self._days} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._days


rose = Plant("Rose", 15.0, 30, 0.5)
print("=== Garden Security System ===")
print("Plant created: ", end="")
rose.show()
print()
rose.set_height(30)
rose.set_age(60)
print()
rose.set_height(-1)
rose.set_age(-1)
print()
print("Current state: ", end="")
rose.show()
