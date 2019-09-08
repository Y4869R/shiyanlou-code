#!/usr/bin/env python3

# Extract the number in the string in the file and print the output.
# author: mlgc4869
# date: 2019-09-08

#fd = open('./String.txt')
#stringout = ''
#for line in fd:
#    for i in line:
#        if i.isdigit():
#            stringout += i
#fd.close()

#print(stringout)

with open('/tmp/String.txt') as f:
    s = f.read()

res = ""

for chr in s:
    if chr.isdigit():
        res += chr

print(res)

