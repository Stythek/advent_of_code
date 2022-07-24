"""
2022-07-23 Author: Steffen Hytrek
"""

with open('./input.txt') as input_file:
    INPUT_STRING = input_file.read()


def part_1() -> None:

    floor_number = 0

    for count, char in enumerate(INPUT_STRING):
        if char == "(":
            floor_number += 1
        elif char == ")":
            floor_number -= 1
        else:
            print(f"Some kind of error with char (pos: {count}): {char}")
            break
    print(f"Final floor is: {floor_number}")


def part_2() -> None:

    floor_number = 0

    for count, char in enumerate(INPUT_STRING):
        if char == "(":
            floor_number += 1
        elif char == ")":
            floor_number -= 1
        else:
            print(f"Some kind of error with char (pos: {count}): {char}")
            break
        if floor_number == -1:
            print(f"First time in the basement at char position: {count + 1}")
            break


part_1()
part_2()
