#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too main for plants (min 0°C)")
    return temp


def test_temperature():
    print("=== Garden Temperature ===")
    print("Input data is '25'")
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is 'abc'")
    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("input data is '100'")
    try:
        temperature = input_temperature("100")
        print(f"temperatue is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("input data is '-50'")
    try:
        temperature = input_temperature("-50")
        print(f"temperatue is now {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
