#!/usr/bin/env python3

# read file and print the contents
# author: mlgc4869
# date: 2019-09-08

name = input("Enter the file name: ")
fobj = open(name)
for line in fobj:
    print(line)

fobj.close()

fobj = open(name)
print('*'*20)
print(fobj.read())
fobj.close()

