#!/usr/bin/env python3
class plant:
    name = ""
    height = 0
    growth_rate = 0
    days = 0

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm {self.days} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days += 1


rose = plant()
rose.name = "rose"
rose.height = 3
growth_rate = 0.1
rose.days = 30
print("=== Garden Plant Registry ===")
rose.show()
height = rose.height
for i in range(1, 8):
    print("=== Day", i, "===")
    rose.grow()
    rose.age()
    rose.show()
print("Growth this week:", round(rose.height - height, 1), "cm")
