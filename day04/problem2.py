# Missing the 'cid' field is ok. passport will still be valid.
# Missing any other field is an invalid passport
import string

# Passports can be separated by a blank line
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0
passport = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0}
with open('input.txt') as input_file:
    for line in input_file:
        if line != '\n':  # Determines if it's the end of the current passport data
            line = line.strip().replace(' ', ':').split(':')
            print(line)
            for element in range(len(line)-1):
                if line[element] in passport:
                    # Check if passport data is valid here.
                    if line[element] == 'byr':
                        if 1920 <= int(line[element+1]) <= 2002:
                            passport[line[element]] += 1
                    if line[element] == 'iyr':
                        if 2010 <= int(line[element+1]) <= 2020:
                            passport[line[element]] += 1
                    if line[element] == 'eyr':
                        if 2020 <= int(line[element+1]) <= 2030:
                            passport[line[element]] += 1
                    if line[element] == 'hgt':
                        print(line[element+1][-2:])
                        if line[element+1][-2:] == 'cm':
                            print('passed')
                            if 150 <= int(line[element+1][:-2]) <= 193:
                                passport[line[element]] += 1
                        elif line[element+1][-2:] == 'in':
                            if 59 <= int(line[element+1][:-2]) <= 76:
                                passport[line[element]] += 1
                    if line[element] == 'hcl' and line[element+1][0] == '#':
                        for char in line[element]:
                            if char in string.ascii_lowercase[0:6] or char in string.digits:
                                passport[line[element]] += 1
                    if line[element] == 'ecl':
                        if line[element+1] in eye_colors:
                            passport[line[element]] += 1
                    if line[element] == 'pid':
                        if len(line[element+1]) == 9:
                            passport[line[element]] += 1
        else:  # We hit a blank line. Check if current passport is valid before moving on
            print(f"Checking passport:\n {passport}")
            if 0 in passport.values():
                print("Hit invalid")
            else:
                print("Found valid passport.")
                valid_passports += 1
            for k, v in passport.items():
                passport[k] = 0  # Reset our passport for the next entry


print(valid_passports)
