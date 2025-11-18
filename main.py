#
# def sum(a, b):
#     return(a + b)
# print(sum(3,4))
#
# def sub(c, d):
#     return(c - d)
# print(sub(3,2))
#
# def mul(x,y):
#     return(x * y)
# print(mul(8, 8))
#
# def divide(s,t):
#     return( s/t )
# print(divide(8, 4))
#


array = [1,0,5,4,3,100,9,-9, -1, -99, 20]
largest_number = array[0]
for i in array:
    if i>largest_number:
        largest_number = i
array.sort()
array.reverse()
top_three = array[0:3]
print(largest_number)
print(top_three)
