#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z':")
        parts = text.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
        else:
            values = []
            for part in parts:
                try:
                    values.append(float(part))
                except ValueError as e:
                    print(f"Error on parameter '{part}': {e}")
                    break
                if len(values) == 3:
                    return (values[0], values[1], values[2])


print("=== Game Coordinate System ===")
print()
player = get_player_pos()
print("Get a first set of coordinates")
print(f"Got a first tuple: {player}")
print(f"It includes: X={player[0]}, Y={player[1]}, Z={player[2]}")
print(f"Distance to center: {round(math.sqrt(
      player[0]**2 + player[1]**2 + player[2]**2), 4)}")
print()
print("Distance between the 2 sets of coordinates")
coor = get_player_pos()
print(f"Distance between to 2 of cordinates: {round(math.sqrt(
        (coor[0] - player[0])**2 + (coor[1] - player[1])**2 +
        (coor[2] - player[2])**2), 4)}")
