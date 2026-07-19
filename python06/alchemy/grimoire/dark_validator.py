#!/usr/bin/env python3
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    copy = ingredients.lower()
    for item in allowed:
        if item in copy:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
