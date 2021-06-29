'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''
nums = [1, 1, 0, 1, 1, 1]
max = 0
count = 0
for elem in nums:
    if elem:
        count += 1
        max = count if count > max else max
    else:
        count = 0
print(max)
