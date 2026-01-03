# a = int(input())
# square = a * a
# print(square)

# x = int(input())
# y = int(input())
# if x> y:
#     print(x)
# else:
#     print(y)

# q= int(input())
# if q%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

# Take three numbers.
# Print the biggest number.

# x = int(input())
# y = int(input())
# z = int(input())
#
# if x > y and x > z:
#     print(x)
# elif y > x and y > z:
#     print(y)
# else:
#     print(z)


# Take one number.
# Print all numbers from 1 to that number

# p = int(input())
# for i in range(1, p+1):
#     print(i)

# Take one number.
# Print the sum of all numbers from 1 to that number.

# t = int(input())
#
# total = 0
#
# for r in range(1, t + 1):
#     total = total + r
#
# print(total)

# Take one number n.
# Count how many even numbers are there from 1 to n.
# Print the count.

# a = int(input())
# count =0
# for i in range(1, a+1):
#     if i%2==0:
#         count = count +1
# print(count)

# Take one number n.
# Print the sum of all even numbers from 1 to n.

# i = int(input())
# sum =0
# for r in range(1, i+1):
#     if r%2==0:
#         sum = sum + r
# print(sum)

# 2 4 6 8 1


# Take one number n.
# Print all numbers from 1 to n that are divisible by both 3 and 5.
#
# Example
# Input: 20
# Output:
# 15



# o = int(input())
# for i in range(1, o+1):
#     if i%3==0 and i%5==0:
#         print(i)
#

# nums = [2, 7, 11, 15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i,j)

# nums = [2, 7, 11, 15]
# target = 9
# seen={}
# for i in range(len(nums)):
#     needed = target-nums[i]
#     if needed in seen:
#         print(seen[needed], i)
#         break
#     else:
#         seen[nums[i]] = i

# Given a list of numbers, return true if any number appears more than once.
#
# Example
# nums = [1, 2, 3, 1]
# Output: true

nums = [1, 2, 3, 1]
seen = set()
for i in nums:
    if i in seen:
        print(True)
        break
    seen.add(i)
else:
    print(False)