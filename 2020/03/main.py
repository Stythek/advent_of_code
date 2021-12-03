import math
import copy


def toboggan_trajectory_one():
    tree_count_short = 0
    empty_count_short = 0
    tree_count_long = 0
    empty_count_long = 0
    final_map_short = []

    with open('./input.txt') as f:
        for line in f:
            final_map_short.append(list(line.strip()))

    final_map_long = copy.deepcopy(final_map_short)
    initial_map = copy.deepcopy(final_map_short)

    width = len(final_map_short[0])
    height = len(final_map_short)

    repetitions = math.ceil((height / width)*3)
    i = 1

    while i < repetitions:
        for index, line in enumerate(final_map_long):
            final_map_long[index] = line + initial_map[index]
        i += 1

    # [x,y]
    cursor_long = [0, 0]
    cursor_short = [0, 0]

    while cursor_long[0] < height:
        if cursor_long[0] == 0:
            cursor_long[0] += 1
            cursor_long[1] += 3
            continue
        if final_map_long[cursor_long[0]][cursor_long[1]] == '#':
            final_map_long[cursor_long[0]][cursor_long[1]] = 'X'
            tree_count_long += 1
        elif final_map_long[cursor_long[0]][cursor_long[1]] == '.':
            final_map_long[cursor_long[0]][cursor_long[1]] = 'O'
            empty_count_long += 1
        cursor_long[0] += 1
        cursor_long[1] += 3

    while cursor_short[0] < height:
        if cursor_short[0] == 0:
            cursor_short[0] += 1
            cursor_short[1] = (cursor_short[1] + 3) % width
            continue
        if final_map_short[cursor_short[0]][cursor_short[1]] == '#':
            final_map_short[cursor_short[0]][cursor_short[1]] = 'X'
            tree_count_short += 1
        elif final_map_short[cursor_short[0]][cursor_short[1]] == '.':
            final_map_short[cursor_short[0]][cursor_short[1]] = 'O'
            empty_count_short += 1
        cursor_short[0] += 1
        cursor_short[1] = (cursor_short[1] + 3) % width

    for index, line in enumerate(final_map_long):
        if not('X' in line or 'O' in line):
            print(f'(long) Error in line {index}')

    for index, line in enumerate(final_map_short):
        if not('X' in line or 'O' in line):
            print(f'(short) Error in line {index}')

    print(
        f'Long version: Empty={empty_count_long}, Trees={tree_count_long}, overall={empty_count_long+tree_count_long}')
    print(
        f'Short version: Empty={empty_count_short}, Trees={tree_count_short}, overall={empty_count_short+tree_count_short}')
    print(5*'-' + 'Part One'+5*'-')


def toboggan_trajectory_two():
    tree_count = []
    empty_count = []
    final_map = []
    variants = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]
    for index, variant in enumerate(variants):
        temp = []
        with open('./input.txt') as f:
            for line in f:
                temp.append(list(line.strip()))
        final_map.append(temp)

    initial_map = copy.deepcopy(final_map)

    width = len(initial_map[0][0])
    height = len(initial_map[0])

    # [x,y]
    cursor = [0, 0]

    for index, variant in enumerate(variants):
        if index+1 > len(tree_count):
            tree_count.append(0)
        if index+1 > len(empty_count):
            empty_count.append(0)
        while cursor[0] < height:
            if cursor[0] == 0:
                cursor[0] = cursor[0] + variant[0]
                cursor[1] = (cursor[1] + variant[1]) % width
                continue
            if final_map[index][cursor[0]][cursor[1]] == '#':
                final_map[index][cursor[0]][cursor[1]] = 'X'
                tree_count[index] += 1
            elif final_map[index][cursor[0]][cursor[1]] == '.':
                final_map[index][cursor[0]][cursor[1]] = 'O'
                empty_count[index] += 1
            cursor[0] = cursor[0] + variant[0]
            cursor[1] = (cursor[1] + variant[1]) % width
        cursor = [0, 0]

    for index, variant in enumerate(variants):
        print(
            f'Variant {variant}: Trees={tree_count[index]}, Overall={tree_count[index]+empty_count[index]}')

    print(f'The product of all slopes: {math.prod(tree_count)}')


toboggan_trajectory_one()
toboggan_trajectory_two()
