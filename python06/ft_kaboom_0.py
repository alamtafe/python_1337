#!/usr/bin/env python3
import alchemy.grimoire


print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(
        f"Testing record light spell: "
        f"{alchemy.grimoire.light_spell_record(
            'fantasy',
            'Earth, wind and fire'
        )}"
)
