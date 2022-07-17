
def password_philosophy_one():
    count = 0
    with open('./input.txt') as f:
        for line in f:
            min_count = int(line.split('-')[0])
            max_count = int(line.split(' ')[0].split('-')[-1])
            letter = line.split(':')[0].split(' ')[-1]
            password = line.split(' ')[-1]
            if min_count <= password.count(letter) <= max_count:
                count += 1
    print('Old valid: ', count)


def password_philosophy_two():
    count = 0
    count_false = 0
    with open('./input.txt') as f:
        for line in f:
            pos_one = int(line.split('-')[0])
            pos_two = int(line.split(' ')[0].split('-')[-1])
            letter = line.split(':')[0].split(' ')[-1]
            password = line.split(' ')[-1]
            if pos_two > len(password):
                print("Index out of bounds")
                continue
            if password[pos_one-1] == letter and password[pos_two-1] != letter:
                count += 1
            elif password[pos_one-1] != letter and password[pos_two-1] == letter:
                count += 1
            elif password[pos_one-1] != letter and password[pos_two-1] != letter:
                count_false += 1
            elif password[pos_one-1] == letter and password[pos_two-1] == letter:
                count_false += 1
    print('Valid: ', count)
    print('Invalid: ', count_false)


password_philosophy_one()
password_philosophy_two()
