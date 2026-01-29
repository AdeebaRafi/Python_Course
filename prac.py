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

# nums = [1, 2, 3, 1]
# seen = set()
# for i in nums:
#     if i in seen:
#         print(True)
#         break
#     seen.add(i)
# else:
#     print(False)



# Given two strings, check if one is an anagram of the other.
#
# Example
# s = "anagram"
# t = "nagaram"
# Output: true

s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)
else:
    count = {}

    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in t:
        if c not in count:
            print(False)
            break
        count[c] -= 1
        if count[c] < 0:
            print(False)
            break
    else:
        print(True)

# You are given prices of a stock each day.
# You can buy once and sell once.
# Find maximum profit.
#
# Example
# prices = [7, 1, 5, 3, 6, 4]
# Output: 5
prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)

#  [1, 2, 3, 4, 5] Reverse an array

# arr = [1, 2, 3, 4, 5]
# left = 0
# right = len(arr)-1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#
#     left +=1
#     right -=1
# print(arr)

# hello
s = "hello"
lst = list(s)

left = 0
right = len(lst) - 1

while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1

result = "".join(lst)
print(result)


s = "python"

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)

nums = [0, 1, 0, 3, 12]

pos = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[pos] = nums[i]
        pos += 1

while pos < len(nums):
    nums[pos] = 0
    pos += 1

print(nums)


# nums = [2, 1, 5, 1, 3, 2]
# k = 3
#
# window_sum = sum(nums[:k])
# max_sum = window_sum
#
# for i in range(k, len(nums)):
#     window_sum = window_sum + nums[i] - nums[i - k]
#     if window_sum > max_sum:
#         max_sum = window_sum
#
# print(max_sum)


nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 2
window_sum = sum(nums[:k])
max_sum = window_sum
for i in range(k, len(nums)):
    window_sum= window_sum+nums[i]- nums[i-k]
    if window_sum>max_sum:
        max_sum = window_sum
print(max_sum)


s = "abba"


seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
## 14 jan practice

nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
min_len = float("inf")

for right in range(len(nums)):
    current_sum += nums[right]

    while current_sum >= target:
        min_len = min(min_len, right - left + 1)
        current_sum -= nums[left]
        left += 1

if min_len == float("inf"):
    print(0)
else:
    print(min_len)
## hello
##
# nums = [1, 4, 4]
# target = 4

## Adeeba
##
nums = input("Enter numbers with space: ")
nums = nums.split()
nums = [int(x) for x in nums]

s = 0
for e in nums:
    if e % 2 == 0:
        s += e

print("Sum of even numbers:", s)

def number(j):
    if(j%2==0):
        return True
    else:
        return False
x = int(input("Enter a number: "))
print(number(x))

print("Sum of even numbers:", s)

def number(j):
    if(j%2==0):
        return True
    else:
        return False
x = int(input("Enter a number: "))
print(number(x))

nums = input("Enter numbers with space: ")
nums = nums.split()
nums = [int(x) for x in nums]

s = 0
for e in nums:
    if e % 2 == 0:
        s += e

print("Sum of even numbers:", s)
