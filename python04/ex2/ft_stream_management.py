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
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        name = sys.stdin.readline().strip()
        if name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{name}'")
            try:
                new_file: typing.IO = open(name, "w")
                new_file.write(new_text)
                new_file.close()
                print(f"Data saved in file '{name}'.")
            except Exception as e:
                sys.stderr.write("[STDERR] Error opening")
                sys.stderr.write(f"file '{name}': {e}\n")
                print("Data not saved.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
