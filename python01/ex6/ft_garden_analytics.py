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
        self.stats = Plant.Statistics()

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm {self._days} days old")
        self.stats.show_calls += 1

    class Statistics:

        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats : {self.grow_calls} grow", end=" ")
            print(" {self.age_calls} days,", end=" ")
            print(f"{self.show_calls} show")

    def grow(self):
        self._height += self.growth_rate
        self.stats.grow_calls += 1

    def age(self):
        self._days += 1
        self.stats.age_calls += 1

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

    @staticmethod
    def is_year_old(n):
        if (n < 365):
            print(f"is {n} days more than a year? -> False")
        else:
            print(f"is {n} days more than a year? -> True")

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0, 0, 0)

    def display(self):
        self.stats.display()


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
            print(f"{self.name} has bloming beautifully!")


class Seed(Flower):

    def __init__(self, name, height, days, growth_rate, color):
        super().__init__(name, height, days, growth_rate, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):

    def __init__(self, name, height, days, growth_rate, trunk_diameter):
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.produce_shade_call = 0

    def show(self):
        super().show()
        print(f"Trunk diameter : {self.trunk_diameter}")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of", end=" ")
        print(f"{self.get_height()}cm long and", end=" ")
        print(f"{self.trunk_diameter}cm wide.")
        self.produce_shade_call += 1

    def display(self):
        super().display()
        print(f"{self.produce_shade_call} shade")


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


def display_statistics(plnt):
    plnt.display()


print("=== Garden Plant Types ===")
Plant.is_year_old(30)
Plant.is_year_old(400)
print()
print("===Flower")
rose = Flower("Rose", 15.0, 30, 0.5, "red")
rose.show()
print("{Statistics for Rose}")
display_statistics(rose)
print("[asking the rose grow  and  bloom]")
rose.bloom()
rose.grow()
rose.show()
print("{Statistics for Rose}")
display_statistics(rose)
print()
print("==Tree")
oak = Tree("Oak", 200.0, 50, 5.0, 0.5)
oak.show()
print("{Statistics for Oak}")
display_statistics(oak)
print("[asking the oak to produce shade]")
oak.produce_shade()
print("{Statistics for Oak}")
display_statistics(oak)
print()
print("=== Seed")
sunflower = Seed("sunflower", 30.0, 20, 2.0, "yellow")
sunflower.show()
print("[make sunflower grow, age and blom]")
sunflower.show()
sunflower.age()
sunflower.grow()
sunflower.bloom()
print("{Statistics for Sunflower}")
display_statistics(sunflower)
print()
print("===annoymous")
unknown = Plant.create_anonymous()
unknown.show()
print("{Statistics for Unknown plant}")
display_statistics(unknown)
