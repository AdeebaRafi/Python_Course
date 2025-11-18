# # Find the sum of numbers from 1 to 50
# # Use a while loop.
# from sympy.strategies.core import switch
# from tornado.gen import Return
#
# total = 50
# number = 1
# while number <= 50:
#     total += number
#     number += 1
# print(f"Sum using while loop: {total}")
#
# count = 0
# for a in range(1,51):
#     count = count + a
#     print(f"Sum using while loop: {count}")
#
# t_sum = sum(range(1,51))
# print(f' use sum method for sum, {t_sum}')

# # Print squares of numbers from 1 to 10
# # (1, 4, 9, 16, …)
# #
# #
# for a in range(1,11):
#     sq = a * a
#     print(sq)

# # Count how many odd numbers are in a list
# # Example list
# # [3, 4, 11, 12, 7, 8]
# # Use a for loop and an if.
#
# a = [3, 4, 11, 12, 7, 8]
# c=0
# for b in a:
#     if b%2 != 0:
#         print(b)
#         c +=1
# print("Odd numbers are", c)

# Print all numbers from 1 to 20
# But when the number is 10, print “stop now”
# Then break the loop.

# for g in range(1,21):
#     print(g)
#     if(g==10):
#         break

# switch(p(range(1,21))):
# case "a":
# print(p)
# if(p==10):
#     break
# else:
#     print("try again")



# Write a function that takes a number
# If the number is even return True
# If not return False
# Use if
# Use return

# def number(j):
#     if(j%2==0):
#         return True
#     else:
#         return False
# x = int(input("Enter a number: "))
# print(number(x))



# Write a function that takes a list of numbers
# Return the sum of only the even numbers
# Use for
# Use if
# Use a total variable

nums = input("Enter numbers with space: ")
nums = nums.split()
nums = [int(x) for x in nums]

s = 0
for e in nums:
    if e % 2 == 0:
        s += e

print("Sum of even numbers:", s)


# Write a function that prints the first n numbers of the pattern
# 1
# 22
# 333
# 4444
# and so on
# Use a loop inside a loop.
# pattern = (1,
#            22,
#            333,
#            4444)
#
# for r in pattern:
#     print(pattern)

