# day 4 (~50 min)
import re


def main():
    with open('input4.txt', 'r') as f:
        passports = [s.replace('\n', ' ').split(' ') for s in f.read().split('\n\n')]
        passports = [dict(zip([s.split(':')[0] for s in passport], [s.split(':')[1] for s in passport])) for passport in passports]

    print('day 4a solution:')
    print(sum([is_valid_1(p) for p in passports]))

    print('day 4b solution:')
    print(sum([is_valid_2(p) for p in passports]))


def is_valid_1(p):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return all([key in p.keys() for key in required_keys])


def is_valid_2(p):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return (
        all([key in p.keys() for key in required_keys])
        and validate_byr(p)
        and validate_iyr(p)
        and validate_eyr(p)
        and validate_hgt(p)
        and validate_hcl(p)
        and validate_ecl(p)
        and validate_pid(p)
    )


def validate_byr(p):
    return re.search("^\\d{4}$", p['byr']) and int(p['byr']) in range(1920, 2003)


def validate_iyr(p):
    return re.search("^\\d{4}$", p['iyr']) and int(p['iyr']) in range(2010, 2021)


def validate_eyr(p):
    return re.search("^\\d{4}$", p['eyr']) and int(p['eyr']) in range(2020, 2031)


def validate_hgt(p):
    if re.search("^\\d+(cm|in)$", p['hgt']):
        if 'cm' in p['hgt']:
            return int(p['hgt'].split('c')[0]) in range(150, 194)
        else:
            return int(p['hgt'].split('i')[0]) in range(59, 77)
    else:
        return False


def validate_hcl(p):
    if re.search("^#[0-9a-f]{6}$", p['hcl']):
        return True
    else:
        return False


def validate_ecl(p):
    if re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", p['ecl']):
        return True
    else:
        return False


def validate_pid(p):
    if re.search("^[0-9]{9}$", p['pid']):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
