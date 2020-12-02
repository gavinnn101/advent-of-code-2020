def find_match(nums):
	for i in range(1, len(nums)):
		for k in range(2, len(nums)):
			if nums[i] + nums[k] == 2020:
				return [nums[i], nums[k]]

nums = []

with open('input.txt') as input_file:
	for line in input_file:
		nums.append(int(line))

print(find_match(nums))
