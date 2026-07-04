#!/usr/bin/env python3
import sys
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
print(f"Total arguments: {len(sys.argv)}")
