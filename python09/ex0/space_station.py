#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


if __name__ == "__main__":
    space = SpaceStation(
            station_id="ID00991",
            name="Space X",
            crew_size=8,
            power_level=70.8,
            oxygen_level=67.2,
            last_maintenance="2026-08-26T16:20:08"
    )
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {space.station_id}")
    print(f"Name: {space.name}")
    print(f"Crew {space.crew_size} people")
    print(f"Power {space.power_level}%")
    print(f"Oxygen {space.oxygen_level}%")
    if space.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not Operational")
    print("========================================")
    print("Expected validation error:")
    try:
        space = SpaceStation(
                station_id=20,
                name="Space X",
                crew_size=100,
                power_level=98.1,
                oxygen_level=67.2,
                last_maintenance="2026-08-26T16:20:08"
        )
    except ValidationError as e:
        e = e.errors()
        for er in e:
            print(er["msg"])
