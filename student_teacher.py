#!/usr/bin/env python3

# inherit
# author: mlgc4869
# date: 2019-09-09

import sys
from collections import Counter

class Person(object):
    def __init__(self, name):
        self.name = name;

    def get_details(self):
        return self.name

    def get_version(self):
        return "aptx4869"

    def get_grade(self):
        pass

class Student(Person):
    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade.upper()

    def get_details(self):
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        cnt = Counter(self.grade)
        print("Pass: {}, Fail: {}".format(cnt['A']+cnt['B']+cnt['C'], cnt['D']))

class Teacher(Person):
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade.upper()

    def get_details(self):
        return "{} teaches {}".format(self.name, ",".join(self.papers))

    def get_grade(self):
        cnt = Counter(self.grade)
        print("A: {}, B: {}, C: {}, D: {}".format(cnt['A'], cnt['B'], cnt['C'], cnt['D']))

#
'''
person1 = Person("miaopasi")
stu1 = Student("mlgc", 'C++', 2012)
tea1 = Teacher('4869', ['c', 'c++'])

print(person1.get_details())
print(stu1.get_details())
print(tea1.get_details())
print(tea1.get_version())
'''

#print grade
if sys.argv[1] == "student":
    stu = Student("mlgc", 'C++', 2012, sys.argv[2])
    stu.get_grade()
elif sys.argv[1] == "teacher":
    tea = Teacher('4869', ['c', 'c++'], sys.argv[2])
    tea.get_grade()

