#!/usr/bin/env python3
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    copy = ingredients.lower()
    for item in allowed:
        if item in copy:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
