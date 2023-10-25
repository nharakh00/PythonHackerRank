import math

print("What are the dimensions of the door mat?")

# Note that in the challenge the first input is an odd natural number
dim = input()
dim = dim.split(" ")

# Change the input dimensions to integers
length = int(dim[0])
width = int(dim[1])
string = "WELCOME"

# Iterate by this number for top and bottom halves
halves = math.floor(length/2)
print(halves)

odd_num = 1
factor_2 = 1

for i in range(halves):
    factor_1 = halves - i

    print("---"*factor_1,end="")
    print(".|." * factor_2,end="")
    print("---"*factor_1,end="")
    print()

    factor_2 = factor_2 + 2


string = string.center(width, "-")
print(string)

factor_3 = factor_2 - 2

for i in range(halves):
    factor_1 = halves - i

    print("---"* (i+1),end="")
    print(".|." * factor_3,end="")
    print("---"*(i+1),end="")
    print()

    factor_3 = factor_3 - 2
    factor_1 = factor_1 + 1








"""
# This is the first version 
for i in range(0, 3):
    for j in range(width):
        print("-",end="")
    print()

string = string.center(width, "-")
print(string)


for i in range(0, 3):
    for j in range(width):
        print("-",end="")
    print()

"""


"""
if isinstance(dim[0],int) and isinstance(dim[1], int):
    print("Both Integers")
else:
    print("Something is wrong")
"""



