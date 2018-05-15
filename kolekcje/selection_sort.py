# selection sort
import random

nums = [random.randint(-100, 100) for i in range(26)]

for i in range(len(nums) - 1):
    min_index = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    if min_index != i:
        min_elem = nums[min_index]
        nums[min_index] = nums[i]
        nums[i] = min_elem

print(nums)
