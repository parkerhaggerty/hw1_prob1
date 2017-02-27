# Author: Parker Haggerty
# Date: 1/27/17
# Assignment 1, Problem 1

import math

# User Input
num= int(input("Please enter an integer: \n"))
sign = '0'

# Make a list and a string output
list = []
output= '0'

# Handles the case of the negative
if num < 0:
    sign = '1'
    num=num*(-1)

# Computes binary representation
while num != 0:
    list.append(num%2)
    num= math.floor(num/2)

# Assembles the number
for i in range(len(list)):
    list[i]= list[i]*(10**i)

# Orders list/Outputs binary Representation
list=list[::-1]
output= str(int(sum(list)))
print("The binary representation of your integer is as follows:")
print(sign + output)

# I chose the integer 134. 
# Results: "The binary representation of your integer is as follows: 010000110"