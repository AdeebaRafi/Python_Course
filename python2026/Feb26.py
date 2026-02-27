# Question:
# Given a list of integers, return True if any number appears at least twice. Otherwise return False.
# Input: [1, 2, 3, 4] → False
# Input: [1, 2, 3, 1] → True
nums = [1, 9, 0, 4]
seen = set()
for num in nums:
    if num in seen:
        print(True)
        break
    seen.add(num)
else:
    print(False)
# How to use Set & why to use it
## A set does not allow duplicate items and the elements are not stored in any particular order

# nums = [1, 9, 1, 4]
# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#
#     return False
#
# result = contains_duplicate(nums)
# print(result)

# Question 2
# Given a string, check if it is a palindrome.
#
# Example:
# "madam" → True
# "hello" → False
#
# Constraint:
# Do not use reverse slicing.

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
text = "MadaM"
print(is_palindrome(text))

# Two Sum Problem
#
# Given an array nums and an integer target, return indices of two numbers such that they add up to target.
#
# Example:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(nums)):
    current = nums[i]
    needed = target-current
    if needed in seen:
        print(seen[needed], i)
        break
    seen[current]=i
# working
# i = 0
# current = 2
# needed = 7
# 7 not in seen
# store {2: 0}
#
# i = 1
# current = 7
# needed = 2
# 2 is in seen
# Answer = [0, 1]

# Problem:
# Check if any number appears twice.
# nums = [1, 2, 3, 1]
def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = 1
    return False
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))

# Write code to count frequency of numbers.
# Example:
# nums = [1, 2, 2, 3, 1, 1]
# Output should be:
# {1: 3, 2: 2, 3: 1}

n = [1, 2, 2, 3, 1, 1]
s={}
for e in n:
    if e in s:
        s[e] +=1
    else:
        s[e]=1
print(s)
