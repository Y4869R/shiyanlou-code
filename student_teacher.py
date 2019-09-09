#!/usr/bin/env python3

# inherit
# author: mlgc4869
# date: 2019-09-09

class Person(object):
    def __init__(self, name):
        self.name = name;

    def get_details(self):
        return self.name

    def get_version():
        return "aptx4869"

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ",".join(self.papers))


#
person1 = Person("miaopasi")
stu1 = Student("mlgc", 'C++', 2012)
tea1 = Teacher('4869', ['c', 'c++'])

print(person1.get_details())
print(stu1.get_details())
print(tea1.get_details())
#print(tea1.get_version())

