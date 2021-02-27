import re


def passport_processing_one():
    input_list = []
    passports = []
    fields_all = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    fields_optional = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open('./input.txt') as f:
        for line in f:
            input_list.append(line.strip())

    tmp = {}

    for line in input_list:
        if len(line.strip()) <= 1:
            passports.append(tmp)
            tmp = {}
            continue
        for props in line.split(' '):
            prop_name = props.split(':')[0]
            prop_value = props.split(':')[1]
            tmp[prop_name] = prop_value
    passports.append(tmp)

    count_valid = 0
    count_optional = 0
    count_invalid = 0

    for passport in passports:
        if all(prop in passport for prop in fields_all):
            count_valid += 1
        elif all(prop in passport for prop in fields_optional):
            count_optional += 1
        else:
            count_invalid += 1

    print(
        f'Valid: {count_valid} + optional: {count_optional} + invalid: {count_invalid}')
    print(f'={count_valid + count_optional + count_invalid}')
    print(f'All passports: {len(passports)}')
    print(f'"Valid" passports: {count_valid + count_optional}')
    print(5*'-' + ' End Part 1 ' + 5*'-')


def passport_processing_two():
    input_list = []
    passports = []
    fields_all = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    fields_optional = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open('./input.txt') as f:
        for line in f:
            input_list.append(line.strip())

    tmp = {}

    for line in input_list:
        if len(line.strip()) <= 1:
            passports.append(tmp)
            tmp = {}
            continue
        for props in line.split(' '):
            prop_name = props.split(':')[0]
            prop_value = props.split(':')[1]
            tmp[prop_name] = prop_value
    passports.append(tmp)

    count_valid = 0
    count_invalid = 0

    reg_hcl = re.compile('^#[a-f0-9]{6}$')
    reg_pid = re.compile('^[0-9]{9}$')

    for passport in passports:
        temp_list = []
        if all(prop in passport for prop in fields_optional):
            temp_list.append(1920 <= int(passport['byr']) <= 2002)
            temp_list.append(2010 <= int(passport['iyr']) <= 2020)
            temp_list.append(2020 <= int(passport['eyr']) <= 2030)
            if len(re.findall('\D+', passport['hgt'])) == 0:
                temp_list.append(False)
            elif 'cm' in re.findall('\D+', passport['hgt']):
                temp_list.append(150 <= int(re.findall(
                    '\d+', passport['hgt'])[0]) <= 193)
            elif 'in' in re.findall('\D+', passport['hgt']):
                temp_list.append(59 <= int(re.findall(
                    '\d+', passport['hgt'])[0]) <= 76)
            temp_list.append(bool(reg_hcl.match(passport['hcl'])))
            temp_list.append(passport['ecl'] in [
                             'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            temp_list.append(bool(reg_pid.match(passport['pid'])))
            if all(temp_list):
                count_valid += 1
            else:
                count_invalid += 1
        else:
            count_invalid += 1
    print(
        f'Valid: {count_valid} + invalid: {count_invalid} ={count_valid + count_invalid}')
    print(f'All passports: {len(passports)}')


passport_processing_one()
passport_processing_two()
