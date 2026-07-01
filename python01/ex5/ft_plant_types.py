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


class Flower(Plant):

    def __init__(self, name, height, days, growth_rate, color):
        super().__init__(name, height, days, growth_rate)
        self.color = color
        self.blom = False

    def bloom(self):
        self.blom = True

    def show(self):
        super().show()
        print(f"Color : {self.color}")
        if (self.blom is False):
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"f{self.name} has bloming beautifully!")


class Tree(Plant):

    def __init__(self, name, height, days, growth_rate, trunk_diameter):
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f"Trunk diameter : {self.trunk_diameter}")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a", end="")
        print(f"shade of {self.get_height()}cm long", end="")
        print(f"and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):

    def __init__(self, name, height, days, growth_rate, harvest_season):
        super().__init__(name, height, days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age(self):
        super().age()
        self.nutritional_value += 1


print("=== Garden Plant Types ===")
print("=== Flower")
rose = Flower("Rose", 15.0, 30, 0.5, "red")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()
print()
print("==Tree")
oak = Tree("Oak", 200.0, 50, 5.0, 0.5)
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print()
print("=== Vegetable")
tomato = Vegetable("Tomato", 1.5, 10, 3.0, "April")
tomato.show()
print("[make tomato grow and age for 20 days]")
for i in range(20):
    tomato.grow()
    tomato.age()
tomato.show()
