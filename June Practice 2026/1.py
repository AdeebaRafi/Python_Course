# Problem 1: Even or Odd
# x = int(input("Enter a number"))
# if x%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# Problem 2: Largest Number
# a = int(input("Enter first number: "))
# b = int(input("Enter second number"))
# if a>b:
#     print("Largest number is", a)
# if b > a:
#     print("Largest number is", b)
# else:
#     print("Both numbers are equal")

#
# Problem 3: Sum of Numbers
# total = 0
# n = int(input("Enter number: "))
# for i in range(1,n+1):
#     total = i + total
# print(total)


# Problem 4: Count Vowels
# count = 0
# vowel = ["a", "e", "i", "o", "u"]
# word = input("Enter a word: ")
# word = word.lower()
# for letter in word:
#     if letter in vowel:
#         count += 1
# print(count)

# Problem 5: Multiplication Table
# total = 1
# n = int(input("Enter number: "))
# for i in range(1,11):
#     total = i * n
#     print(f"{n} x {i} = {total}")


# Problem 6: Positive, Negative, or Zero

# number = int(input("Enter a number: "))
# if number>0:
#     print("Positive number")
# elif number<0:
#         print("Negative number")
# else:
#     print("Zero")

# Problem 7: Sum of Even Numbers
# add = 0
# sum = int(input("Enter a number: "))
# for i in range(1, sum+1):
#     if i%2 == 0:
#         add = i + add
# print(add)

# Problem 8: Reverse a String
# reverse = input("Enter a String: ")
# reversed_text = ""
# for char in reverse:
#     reversed_text = char + reversed_text  # Adds to the front
# print(reversed_text)

# reverse = input("Enter a String: ")
# reverse_text = reverse[::-1]
# print(reverse_text)

# Problem 9: Count Digits
num = int(input("Enter a number: "))
temp = num
count = 0
if num == 0:
    count = 1
else:
    while temp >0:
        count +=1
        temp = temp // 10
print(count)

# Problem 10: Largest of Three Numbers
inp = int(input("Enter a number: "))
if inp >