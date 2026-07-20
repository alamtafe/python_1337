#!/usr/bin/env pyhton3
from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(player_1, player_2) -> None:
    print("Testing battle")
    print(player_1.describe())
    print("vs.")
    print(player_2.describe())
    print(" fight!")
    print(player_1.attack())
    print(player_2.attack())


test_factory(FlameFactory())
print()
test_factory(AquaFactory())
print()
player_1 = FlameFactory()
player_2 = AquaFactory()
test_battle(player_1.create_base(), player_2.create_base())
