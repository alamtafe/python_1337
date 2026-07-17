#!/usr/bin/env python03
import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
try:
    print(f"{alchemy.create_earth()}")
except AttributeError as e:
    print("This will raise an exception!")
    print(f"Testing the hidden create_earth: {e}")
