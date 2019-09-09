#!/usr/bin/env python3

# __init__ funtion in class
# author: mlgc4869
# date: 2019-09-09


class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0, 4.5)

print(x.r, x.i)

