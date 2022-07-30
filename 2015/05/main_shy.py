'''
2022-07-24 Author: Steffen Hytrek
'''

import re

def part_1() -> None:
    VOWELS_REGEX = r'.*([aeiou].*){3,}'
    DOUBLES_REGEX = r'(.)\1'
    BAD_STRINGS_REGEX = r'(ab|cd|pq|xy)'
    count_good_strings = 0

    with open('./input.txt', encoding='utf-8') as input_file:
        # Input is format LxWxH
        for line in input_file:
            line = line.strip().strip('\n')
            # String contains at least 3 vowels (aeiou)
            if not re.search(VOWELS_REGEX, line):
                continue
            # String contains at least one letter that appears twice in a row (aa|bb|...)
            # the pair can be part of a longer "chain"
            doubles_list = re.findall(DOUBLES_REGEX, line)
            # if len(doubles_list) == 0 or len(doubles_list) != len(set(doubles_list)):
            if len(doubles_list) == 0:
                continue
            # String does NOT contain 'ab', 'cd', 'pq', 'xy'
            if re.search(BAD_STRINGS_REGEX, line):
                continue

            count_good_strings += 1

    print(f'Part 1: Found {count_good_strings} good strings.')
    print(40*'-')

def part_2() -> None:
    PAIR_REGEX = r'(..).*\1'
    LETTER_XYX_REGEX = r'(.).\1'
    count_good_strings = 0

    with open('./input.txt', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip().strip('\n')
            # Repeating doubles that do not overlap
            if not re.search(PAIR_REGEX, line):
                continue
            # At least one char repeats with exactly 1 letter between
            if not re.search(LETTER_XYX_REGEX, line):
                continue
            count_good_strings += 1

    print(f'Part 2: Found {count_good_strings} good strings.')


part_1()
part_2()
