def check_valid(line):
	_min = int(line.split('-')[0])
	_max = int(line.split('-')[1].split(' ')[0])
	policy_character = line.split(':')[0][-1]
	password = line.split(':')[1].strip()
	counter = 0

	for character in password:
		if character == policy_character:
			counter += 1

	if counter >= _min and counter <= _max:
		return True

total = 0

with open ('input.txt') as test_cases:
	for line in test_cases:
		if check_valid(line):
			total += 1

print(f"Total valid passwords: {total}")