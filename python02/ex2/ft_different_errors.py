#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('a')
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        'x' + 1
    else:
        return


def test(data: int) -> None:
    try:
        garden_operations(data)
        print("Operation completed successfully")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test(0)
    print("Testing operation 1...")
    test(1)
    print("Testing operation 2...")
    test(2)
    print("Testing operation 3...")
    test(3)
    print("Testing operation 4...")
    test(4)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
#     try:
#         garden_operations(0)
#     except (ValueError, TypeError) as e:
#         print(e)
