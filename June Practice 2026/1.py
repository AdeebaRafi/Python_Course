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
# else:
#     print("Largest number is", b)

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
total = 1
n = int(input("Enter number: "))
for i in range(1,11):
    total = i * n
print(f"{n} x {i} = {total}")

