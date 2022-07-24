import math


def binary_boarding_one():
    print(5*'-' + ' Binary Boarding Part 1 ' + 5*'-')
    input_list = []
    with open('./input.txt', encoding="utf-8") as f:
        for line in f:
            input_list.append(line.strip())

    highest_seat_id = 0

    for boarding_pass in input_list:
        min_row = 0
        max_row = 127
        min_column = 0
        max_column = 7
        row_code = boarding_pass[0:7]
        column_code = boarding_pass[7:]
        row = 0
        column = 0

        for index, char in enumerate(row_code):
            if char == 'F':
                min_row == min_row
                max_row = math.floor(min_row + ((max_row - min_row) / 2))
            if char == 'B':
                min_row = math.ceil(max_row - ((max_row - min_row) / 2))
                max_row = max_row
            if index+1 == len(row_code):
                if char == 'F':
                    row = min_row
                if char == 'B':
                    row = max_row

        for index, char in enumerate(column_code):
            if char == 'L':
                min_column == min_column
                max_column = math.floor(
                    min_column + ((max_column - min_column) / 2))
            if char == 'R':
                min_column = math.ceil(
                    max_column - ((max_column - min_column) / 2))
                max_column = max_column
            if index+1 == len(column_code):
                if char == 'L':
                    column = min_column
                if char == 'R':
                    column = max_column

        highest_seat_id = max(highest_seat_id, (row * 8 + column))

    print(highest_seat_id)
    print(5*'-' + ' End ' + 5*'-')


def binary_boarding_two():
    print(5*'-' + ' Binary Boarding Part 2 ' + 5*'-')
    input_list = []
    with open('./input.txt', encoding="utf-8") as f:
        for line in f:
            input_list.append(line.strip())

    max_seat_id = 127 * 8 + 7
    seat_id_list = []

    for boarding_pass in input_list:
        min_row = 0
        max_row = 127
        min_column = 0
        max_column = 7
        row_code = boarding_pass[0:7]
        column_code = boarding_pass[7:]
        row = 0
        column = 0

        for index, char in enumerate(row_code):
            if char == 'F':
                min_row == min_row
                max_row = math.floor(min_row + ((max_row - min_row) / 2))
            if char == 'B':
                min_row = math.ceil(max_row - ((max_row - min_row) / 2))
                max_row = max_row
            if index+1 == len(row_code):
                if char == 'F':
                    row = min_row
                if char == 'B':
                    row = max_row

        for index, char in enumerate(column_code):
            if char == 'L':
                min_column == min_column
                max_column = math.floor(
                    min_column + ((max_column - min_column) / 2))
            if char == 'R':
                min_column = math.ceil(
                    max_column - ((max_column - min_column) / 2))
                max_column = max_column
            if index+1 == len(column_code):
                if char == 'L':
                    column = min_column
                if char == 'R':
                    column = max_column

        seat_id_list.append((row * 8 + column))

    for seat_id in range(0, max_seat_id+1):
        if not seat_id in seat_id_list:
            if seat_id-1 in seat_id_list and seat_id+1 in seat_id_list:
                print(f'My seat id: {seat_id}')

    print(5*'-' + ' End ' + 5*'-')


binary_boarding_one()
binary_boarding_two()
