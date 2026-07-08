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
        print("File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
