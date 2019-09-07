#!/usr/bin/env python3

# Hadamard product n * n
# author: mlgc4869
# date: 2019-

n = int(input("Enter the value of n: "))

print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])

result = []
for i in range(n):
    result.append([a[i][j] * b[j][i] for j in range(n)])
print("After matrix multiplication")

print("*" * 20)
for x in result:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("*" * 20)

