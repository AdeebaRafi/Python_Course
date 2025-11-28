# for i in range(1,5):
#     for j in range(i):
#         print(i, end="")
#     print()
from main import largest_number

# Print
# *
# **

# for a in range(1,3):
#     for b in range(a):
#         print("*", end="")
#     print()

# Print
# 1
# 12
# 123
# 1234

rows=4
for e in range(1,rows+1):
    for w in range(1, e+1):
        print(w,end="")
    print()

# A
# BB
# CCC
# DDDD

# print(chr(65));

for i in range(4):
    letter = chr(65 + i)
    for j in range(i + 1):
        print(letter, end="")
    print()


# Given a list
# nums = [2, 5, 7, 8, 10, 3]
# Find the sum of all even numbers.
sum =0
nums = [2, 5, 7, 8, 10, 3]
for i in nums:
    if i%2==0:
        sum +=i
print(sum)

# Given a list
# nums = [4, 9, 1, 5, 7]
# Find the largest number without using the max() function.

nums = [4, 9, 1, 5, 7]
largest_number = nums[0]
for e in nums:
    if e>largest_number:
        largest_number=e
        print(largest_number)

# Given a list
# nums = [1, 2, 3, 2, 1, 2]
# Count how many times the number 2 appears.

c=0
num = [2, 2, 3, 2, 1, 2]
for w in num:
    if w == 2:
        c+=1
print(c)

# Given a list
# nums = [3, 6, 9, 2, 4]
# Make a new list with all numbers doubled
# Example result
# [6, 12, 18, 4, 8]

n = [3, 6, 9, 2, 4]
for a in n:
