# Given an array nums and integer k, return the maximum average of any contiguous subarray of size k.
# nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75
nums = [1,12,-5,-6,50,3]
k = 4
for i in range(k):
    current_sum = current_sum + nums[i]
    max_sum = current_sum
for i in range(k, len(nums)):

