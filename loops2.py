# Find the sum of numbers from 1 to 50
# Use a while loop.

total = 50
number = 1
while number <= 50:
    total += number
    number += 1
print(f"Sum using while loop: {total}")

count = 0
for a in range(1,51):
    count = count + a
    print(f"Sum using while loop: {count}")

t_sum = sum(range(1,51))
print(f'use sum method for sum, {t_sum}')

# Print squares of numbers from 1 to 10
# (1, 4, 9, 16, …)
#
#
for a in range(1,11):
    sq = a * a
    print(sq)

# Count how many odd numbers are in a list
# Example list
# [3, 4, 11, 12, 7, 8]
# Use a for loop and an if.

a = [3, 4, 11, 12, 7, 8]
c=0
for b in a:
    if b%2 != 0:
        print(b)
        c +=1
print("Odd numbers are", c)
