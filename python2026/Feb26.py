# Question:
# Given a list of integers, return True if any number appears at least twice. Otherwise return False.
# Input: [1, 2, 3, 4] → False
# Input: [1, 2, 3, 1] → True
# nums = [1, 9, 0, 4]
# seen = set()
# for num in nums:
#     if num in seen:
#         print(True)
#         break
#     seen.add(num)
# else:
#     print(False)
# How to use Set & why to use it
## A set does not allow duplicate items and the elements are not stored in any particular order

nums = [1, 9, 1, 4]
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

result = contains_duplicate(nums)
print(result)