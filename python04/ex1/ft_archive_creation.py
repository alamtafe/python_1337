#!/usr/bin/env python3
import sys
import typing


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file: typing.IO = open(sys.argv[1])
        text: str = file.read()
        print("---")
        print()
        print(text, end="")
        print()
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        new_text = text.replace("\n", "#\n")
        print("---")
        print()
        print(new_text, end="")
        print()
        print("---")
        name = input("Enter new file name (or empty): ")
        if name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{name}'")
            new_file: typing.IO = open(name, "w")
            new_file.write(new_text)
            new_file.close()
            print(f"Data saved in file '{name}'.")
    except Exception as e:`
        print(f"Error opening file '{sys.argv[1]}': {e}")
