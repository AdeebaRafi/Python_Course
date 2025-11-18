def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-8)
check_number(8)
check_number(0)

# Check if a number is even or odd

def Even_Odd(num):
    if(num%2) == 0:
        print("Even number")
    elif (num % 2) != 0:
        print("Odd Number")

Even_Odd(14)
Even_Odd(3)
Even_Odd(11)
Even_Odd(20)

# Find the largest numbers

array = [1,0,5,4,3,100,9,-9, -1, -99, 20]
largest_number = array[0]
for i in array:
    if i>largest_number:
        largest_number = i
print(largest_number)

array.sort()
array.reverse()
# Find the largest of three numbers

top_three = array[0:3]
lower_three = array[-3:]
print(f"top 3 largest numbers are: {top_three}" )
print(f"lower 3 largest numbers are: {lower_three}" )

# Check if a year is a leap year

def leap_year(year):
    return (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)
print(leap_year(100))
print(leap_year(2000))
print(leap_year(2020))
print(leap_year(2010))


