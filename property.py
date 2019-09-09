#!/usr/bin/env python3

# property
# author: mlgc4869
# date: 2019-09-09

class Account(object):
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        return self.__amt

    @property
    def cny(self):
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=6.6)
    acc.amount = 20
    print("Dollar amount: ", acc.amount)
    print("In CNY: ", acc.cny)
    acc.amount = -100
    print("Dollar amount: ", acc.amount)

