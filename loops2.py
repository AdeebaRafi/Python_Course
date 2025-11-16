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

