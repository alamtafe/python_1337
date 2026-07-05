#!/usr/bin//env python3
import sys


def gen_player_inventory() -> dict:
    inventory = {}
    for arg in sys.argv[1:]:
        try:
            parts = arg.split(":")
            if len(parts) != 2:
                print(f"Error - invalid parameter '{parts[0]}'")
            else:
                item = parts[0]
                qte = int(parts[1])
                if item in inventory:
                    print(f"Redundant item '{item}' - discarding")
                else:
                    inventory[item] = qte
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
    return inventory


print("=== Inventory System Analysis ===")
inventory = gen_player_inventory()
print(f"Got inventory: {inventory}")
item = list(inventory.keys())
print(f"Item list: {item}")
total_qte = sum(inventory.values())
print(f"Total quantity of the {len(item)} items: {total_qte}")
qte = list(inventory.values())

if len(inventory) != 0:
    i = 0
    for arg in item:
        print(f"Item {arg} represents {round((qte[i] / total_qte)*100, 1)}%")
        i += 1
    most = inventory[item[0]]
    key = item[0]
    for arg in inventory.keys():
        if inventory[arg] > most:
            most = inventory[arg]
            key = arg
    print(f"Item most abundant: {key} with quantity {most}")
    least = inventory[item[0]]
    key = item[0]
    for arg in inventory.keys():
        if inventory[arg] < least:
            least = inventory[arg]
            key = arg
    print(f"Item least abundant: {key} with quantity {least}")
inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
