#!/usr/bin/env python3

# string control
# author: mlgc4869
# date: 2019-09-07

s = "miao pa si"
print(s.title())

print(s.upper())

s = "1234"
print(s.isdigit())

s = "CHINA"
print(s.isupper())

s = "GNU/Linux is great"
print("-".join(s.split()))

s = " a bc\n"
print(s.strip())

s = "faulty for a reason"
print(s.find("for"))
print(s.find("miaopasi"))   # return -1 if cannot find
print(s.startswith("re"))
print(s.endswith("son"))

