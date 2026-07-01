#!/usr/bin/env python3
class plant:
    name = ""
    height = 0
    days = 0

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm {self.days} days old")


rose = plant()
rose.name = "rose"
rose.height = 25
rose.days = 20
sunflower = plant()
sunflower.name = "sunflower"
sunflower.height = 18
sunflower.days = 15
cactus = plant()
cactus.name = "cactus"
cactus.height = 12
cactus.days = 120
print("=== Garden Plant Registry ===")
rose.show()
sunflower.show()
cactus.show()
