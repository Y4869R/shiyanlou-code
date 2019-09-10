#!/usr/bin/env python3

# my fact module
# author: mlgc4869
# date: 2019-09-10

def factorial(num):
    """
    返回给定数字的阶乘值
    :arg num: 我们要计算的整数值
    :return: 阶乘值，若参数是负数，则返回-1
    """

    if num < 0:
        return -1
    else:
        if num == 0:
            return 1
        return num * factorial(num - 1)

