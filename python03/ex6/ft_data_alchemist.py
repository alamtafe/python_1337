#!usr/bin/env python3
import random


players = ['Alice',
           'bob',
           'Charlie',
           'dylan',
           'Emma',
           'Gregory',
           'john',
           'kevin',
           'Liam']
print("=== Game Data Alchemist ===")
print(f"Initial list of players: {players}")
name_cpt = [arg.capitalize() for arg in players]
print(f"New list with all names capitalized: {name_cpt}")
name = [arg for arg in players if arg == arg.capitalize()]
print(f"New list of capitalized names only {name}")
scores = {arg: random.randint(0, 1000) for arg in name_cpt}
print(f"Score dict: {scores}")
values = list(scores.values())
average = round(sum(values) / len(values), 2)
print(f"Score average is {average}")
avg_scores = {arg: scores[arg]
              for arg in name_cpt
              if scores[arg] >= average}
print(f"High scores: {avg_scores}")
