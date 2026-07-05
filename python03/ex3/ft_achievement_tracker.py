#!/usr/bin/env python3
import random


def gen_player_achievements() -> set:
    achievemnt = ['Crafting Genius', 'Strategist', 'World Savior',
                  'Speed Runner', 'Survivor', 'Master Explorer',
                  'Treasure Hunter', 'Unstoppable',
                  'First Steps', 'Collector Supreme',
                  'Untouchable', 'Sharp Mind', 'Boss Slayer']
    count = random.randint(5, 8)
    return set(random.sample(achievemnt, count))


print("=== Achievement Tracker System ===")
print()
alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()
print(f"Player Alice: {alice}")
print(f"player Bob: {bob}")
print(f"player Charlie: {charlie}")
print(f"player Dylan : {dylan}")
unique = alice.union(bob, charlie, dylan)
print()
print(f"All distinct achievements: {unique}")
print()
shared = alice.intersection(bob, charlie, dylan)
print(f"Common achievements: {shared}")
print()
only = alice.difference(bob, charlie, dylan)
print(f"Only Alice has: {only} ")
only = bob.difference(alice, charlie, dylan)
print(f"Only bob has : {only}")
only = charlie.difference(alice, bob, dylan)
print(f"Only Charlie has : {only}")
only = dylan.difference(alice, bob, charlie)
print(f"Only Dylan has : {only}")
print()
missing = unique.difference(alice)
print(f"Alice is missing: {missing}")
missing = unique.difference(bob)
print(f"Bob is missing: {missing}")
missing = unique.difference(charlie)
print(f"Charlie is missing: {missing}")
missing = unique.difference(dylan)
print(f"Dylan is missing: {missing}")
