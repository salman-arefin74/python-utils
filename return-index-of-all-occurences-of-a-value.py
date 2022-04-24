nums = [3,4,9,1,3,9,5]
key = 9

indices = [i for i, x in enumerate(nums) if x == key]

print(indices)