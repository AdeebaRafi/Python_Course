# for i in range(1,5):
#     for j in range(i):
#         print(i, end="")
#     print()

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



