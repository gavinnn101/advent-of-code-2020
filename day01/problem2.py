def find_match(nums):
	cnt = 0
	while cnt < len(nums):
		for i in range(1, len(nums)):
			for k in range(2, len(nums)):
				if nums[cnt] + nums[i] + nums[k] == 2020:
					return [nums[cnt], nums[i], nums[k]]
		cnt += 1

nums = []

with open('input.txt') as input_file:
	for line in input_file:
		nums.append(int(line))

print(find_match(nums))
