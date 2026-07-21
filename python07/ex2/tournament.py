#!/usr/bin/envi python3
from ex2 import (
                        FlameFactory,
                        AquaFactory,
                        HealingCreatureFactory,
                        TransformCreatureFactory,
                        NormalStrategy,
                        AggressiveStrategy,
                        DefensiveStrategy,
                        CreatureFactory,
                        BattleStrategy

)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    creatures = []
    for opponent in opponents:
        factory, stratgey = opponent
        creatures.append((factory.create_base(), stratgey))
    length = len(creatures)
    print(f"{length} opponents involved")
    for i in range(length):
        opponent_1, stratgey_1 = creatures[i]
        for j in range(i + 1, length):
            opponent_2, stratgey_2 = creatures[j]
            print()
            print("* Battle *")
            print(opponent_1.describe())
            print("vs.")
            print(opponent_2.describe())
            print("now fight!")
            stratgey_1.act(opponent_1)
            stratgey_2.act(opponent_2)
        i += 1


print("Tournament 0 (basic)")
print(" [ (Flameling+Normal), (Healing+Defensive) ]")
opponents = [
                (FlameFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())
]
battle(opponents)
print("Tournament 1 (error)")
print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
opponents = [
                (FlameFactory(), AggressiveStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())
]
try:
    battle(opponents)
except Exception as e:
    print(f"Battle error, aborting tournament: {e}")
print()
print("Tournament 2 (multiple)")
print(
        " [ (Aquabub+Normal), "
        "(Healing+Defensive), "
        "(Transform+Aggressive) ]"
)
opponents = [
                (AquaFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy()),
                (TransformCreatureFactory(), AggressiveStrategy())
]
battle(opponents)
