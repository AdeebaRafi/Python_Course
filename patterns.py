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

list = [3, 6, 9, 2, 4]
new_list = []
for a in list:
    new_list.append(a*2)
print(new_list)

# Given a string
# s = "hello world"
# Count how many times the letter 'l' appears.

s = "hello world"
cont=0
for a in s:
    if a == 'l':
        cont+=1
print(cont)

# Given a string
# s = "python"
# Print the string in reverse.

s = "python"
for i in range(len(s) -1, -1, -1):
    print(s[i])

s = "adeeba"
rev= ""
for m in range(len(s) -1,-1,-1):
    rev = rev + s[m]
print(rev)

s = "ehsan"
rev = ""
l= len(s)-1
while l>=0:
    rev = rev + s[l]
    l-=1
print(rev)

s = "nomi"
rev = s[::-1]
print(rev)

# Given a string
# s = "open ai"
# Remove all spaces and print the result
s = " open ai "
no_space = s.replace(" ","")
print(no_space)

# Given a string
# s = "banana"
# Find the first index where 'n' appears.
s = "banana"
for a in range(len(s)):
    if s[a] == 'n':
        print(a)
        break


s = "banana"

for i in range(len(s)):
    if s[i] == "n":
        print("index is", i)
        break

for i in range(4):
    # Get the letter from number (65 is A)
    letter = chr(65 + i)
    # Print the letter (i+1) times
    for j in range(i + 1):
        print(letter, end="")
    print()  # Move to the next line

