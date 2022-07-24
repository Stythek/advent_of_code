"""
2022-07-23 Author: Steffen Hytrek
"""

with open('./input.txt', encoding="utf-8") as input_file:
    INPUT_STRING = input_file.read()


def part_1() -> None:
    # Well some of this logic is not needed :facepalm:
    # Should've read the puzzle first :D
    duplicate_count = 0
    visited_houses = {
    }
    current_coords = (0, 0)
    # Set start drop off
    visited_houses[current_coords] = 1

    for count, direction in enumerate(INPUT_STRING):
        new_coords = current_coords
        if direction == "^":
            new_coords = (current_coords[0], current_coords[1] + 1)
        elif direction == "v":
            new_coords = (current_coords[0], current_coords[1] - 1)
        elif direction == ">":
            new_coords = (current_coords[0] + 1, current_coords[1])
        elif direction == "<":
            new_coords = (current_coords[0] - 1, current_coords[1])
        else:
            print(f"Something went wrong (at {count}): {direction}")
            break

        if new_coords in visited_houses:
            duplicate_count += 1
            visited_houses[new_coords] += 1
        elif new_coords not in visited_houses:
            visited_houses[new_coords] = 1
        else:
            print(
                f"Something went wrong with the dict(at {count}): {direction}")
            break
        current_coords = new_coords

    print(f"There were {len(visited_houses)} houses visited.")


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def part_2() -> None:
    duplicate_count = 0
    visited_houses = {
    }
    curr_santa_coords = (0, 0)
    curr_robot_coords = (0, 0)
    # Set start drop off
    visited_houses[(0, 0)] = 2

    # This is some unoptimized pile of code
    for santa_direction, robot_direction in chunker(INPUT_STRING, 2):
        new_santa_coords = curr_santa_coords
        if santa_direction == "^":
            new_santa_coords = (curr_santa_coords[0], curr_santa_coords[1] + 1)
        elif santa_direction == "v":
            new_santa_coords = (curr_santa_coords[0], curr_santa_coords[1] - 1)
        elif santa_direction == ">":
            new_santa_coords = (curr_santa_coords[0] + 1, curr_santa_coords[1])
        elif santa_direction == "<":
            new_santa_coords = (curr_santa_coords[0] - 1, curr_santa_coords[1])
        else:
            print(f"Something went wrong: {santa_direction}")
            break

        new_robot_coords = curr_robot_coords
        if robot_direction == "^":
            new_robot_coords = (curr_robot_coords[0], curr_robot_coords[1] + 1)
        elif robot_direction == "v":
            new_robot_coords = (curr_robot_coords[0], curr_robot_coords[1] - 1)
        elif robot_direction == ">":
            new_robot_coords = (curr_robot_coords[0] + 1, curr_robot_coords[1])
        elif robot_direction == "<":
            new_robot_coords = (curr_robot_coords[0] - 1, curr_robot_coords[1])
        else:
            print(f"Something went wrong: {robot_direction}")
            break

        if new_santa_coords in visited_houses:
            duplicate_count += 1
            visited_houses[new_santa_coords] += 1
        elif new_santa_coords not in visited_houses:
            visited_houses[new_santa_coords] = 1
        else:
            print(f"Something went wrong: {santa_direction}")
            break
        curr_santa_coords = new_santa_coords

        if new_robot_coords in visited_houses:
            duplicate_count += 1
            visited_houses[new_robot_coords] += 1
        elif new_robot_coords not in visited_houses:
            visited_houses[new_robot_coords] = 1
        else:
            print(f"Something went wrong: {robot_direction}")
            break
        curr_robot_coords = new_robot_coords

    print(f"There were {len(visited_houses)} houses visited.")


part_1()
part_2()  # 1150 is too low
