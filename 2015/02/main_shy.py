"""
2022-07-23 Author: Steffen Hytrek
"""


def part_1() -> None:
    square_len_paper = 0

    with open('./input.txt', encoding="utf-8") as input_file:
        # Input is format LxWxH
        for line in input_file:
            box_length, box_width, box_height = [
                int(x) for x in line.split("x")]

            # Formula for calculating surface area of a "right rectangular prism":
            # 2*L*W + 2*W*H + 2*H*L
            side_top_bottom = box_length * box_width
            side_front_back = box_width * box_height
            side_left_right = box_height * box_length
            box_surface = 2 * side_top_bottom + 2 * side_front_back + 2 * \
                side_left_right + min(side_top_bottom,
                                      side_front_back, side_left_right)
            square_len_paper += box_surface

        print(f"Req. square length: {square_len_paper}")


def part_2() -> None:
    len_ribbon = 0

    with open('./input.txt', encoding="utf-8") as input_file:
        # Input is format LxWxH
        for line in input_file:
            # Formula for ribbon is 2*{shortest side} + 2* {medium side}
            box_length, box_width, box_height = [
                int(x) for x in line.split("x")]

            min_side_1, min_side_2 = sorted([box_length, box_width, box_height])[
                :2]

            # Length of ribbon for bow is L*W*H (cubic length of volume)
            len_present_bow = box_length * box_width * box_height

            len_present_ribbon = 2 * min_side_1 + 2 * min_side_2 + len_present_bow
            len_ribbon += len_present_ribbon

        print(f"Req. length of ribbon: {len_ribbon}")


part_1()
part_2()
