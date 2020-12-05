# Missing the 'cid' field is ok. passport will still be valid.
# Missing any other field is an invalid passport

# Passports can be separated by a blank line
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0
passport = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0}
with open('input.txt') as input_file:
    for line in input_file:
        # print(line)
        if line != '\n':
            line = line.strip().replace(' ', ':').split(':')
            # print(line)
            for element in line:
                if element in passport:
                    passport[element] += 1
            # print(passport)
        else:  # We hit a blank line. Check if current passport is valid before moving on
            print(f"Checking passport:\n {passport}")
            if 0 in passport.values():
                print("Hit invalid")
            else:
                print(f"Passport + 1")
                valid_passports += 1
            for k, v in passport.items():
                passport[k] = 0  # Reset our passport for the next entry


print(valid_passports)
