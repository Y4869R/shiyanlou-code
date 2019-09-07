#!/usr/bin/env python3

# for string palindrome
# author: mlgc4869
# date: 2019-09-07

s = input("Please enter a string: ")
z = s[::-1]     # s[::-1] 相当于 s[-1:-len(a)-1:-1]

if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

