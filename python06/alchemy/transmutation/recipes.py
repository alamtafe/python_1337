#!/usr/bin/env python3
from ..elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    return (
            f"Recipe transmuting Lead to"
            f" Gold: brew '{create_air()}' and "
            f"'{strength_potion()}' mixed with '{create_fire()}'"
    )
