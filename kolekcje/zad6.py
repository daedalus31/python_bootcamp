nums_start = [4, 5, 6, 34, 2, 1, 0, 3]

# no loop
print('without loop')
nums = nums_start.copy()
print(nums)
max_elem_index = nums.index(max(nums))
max_elem = max(nums)
min_elem_index = nums.index(min(nums))

nums[max_elem_index] = min(nums)
nums[min_elem_index] = max_elem

print(nums)

# for loop
print('with for loop')
nums = nums_start[::1]
# nums = []
print(nums)
max_elem_index = None
min_elem_index = None

for i in range(len(nums)):
    if max_elem_index is None or nums[i] > nums[max_elem_index]:
        max_elem_index = i
    if min_elem_index is None or nums[i] < nums[min_elem_index]:
        min_elem_index = i

if max_elem_index:
    max_elem = nums[max_elem_index]
    nums[max_elem_index] = nums[min_elem_index]
    nums[min_elem_index] = max_elem

print(nums)
