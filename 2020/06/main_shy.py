def custom_customs_one():
    print(5*'-' + ' Custom Customs Part 1 ' + 5*'-')
    input_list = []
    with open('./input.txt', encoding="utf-8") as f:
        for line in f:
            input_list.append(line.strip())
