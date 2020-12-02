def check_valid(line):
	_min = int(line.split('-')[0])
	_max = int(line.split('-')[1].split(' ')[0])
	policy_character = line.split(':')[0][-1]
	password = line.split(':')[1].strip()
	indices = []

	for character in range(len(password)):
		if password[character] == policy_character:
			indices.append(character+1)

	if (_min in indices and _max not in indices) or (_max in indices and _min not in indices):
		return True

total = 0

with open ('input.txt') as test_cases:
	for line in test_cases:
		if check_valid(line):
			total += 1

print(f"Total valid passwords: {total}")