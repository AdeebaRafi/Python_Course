# Sliding window is used when:
#
# • Problem says subarray or substring
# • Elements must be continuous
# • We need sum, length, max, min


# Given an array nums and integer k, return the maximum average of any contiguous subarray of size k.
# nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75
nums = [1,12,-5,-6,50,3]
k = 4
# Step 1: first window sum
current_sum = 0
for i in range(k):
    current_sum += nums[i]
max_sum = current_sum
# Step 2: slide the window
for i in range(k, len(nums)):
    current_sum = current_sum - nums[i - k] + nums[i]
    max_sum = max(max_sum, current_sum)
print(max_sum / k)