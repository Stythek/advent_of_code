from day_input import InputData


def report_repair_one(data):
    output = {}
    for index, number_one in enumerate(data):
        if index+1 <= len(data):
            if number_one == 1373:
                for number_two in data[index+1:]:
                    if number_one + number_two == 2020:
                        output.update(
                            number_one=number_one, number_two=number_two, multiply=number_one*number_two)

    print("Numbers that == 2020: ", output)


def report_repair_two(data):
    output = {}
    for i_one, number_one in enumerate(data):
        if i_one+1 <= len(data):
            for i_two, number_two in enumerate(data[i_one:]):
                if i_two+1 <= len(data):
                    for number_three in data[i_two:]:
                        if number_one + number_two + number_three == 2020:
                            output.update(
                                number_one=number_one, number_two=number_two, number_three=number_three, multiply=number_one*number_two*number_three)

    print("Numbers that == 2020: ", output)


report_repair_one(InputData.input_numbers)
report_repair_two(InputData.input_numbers)
