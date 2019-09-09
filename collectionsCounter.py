#!/usr/bin/env python3

# collection Counter
# author: mlgc4869
# date: 2019-09-09

from collections import Counter
import re

path = '/usr/lib/python3.5/LICENSE.txt'
words = re.findall('\w+', open(path).read().lower())

#print(words)
most_five_words = Counter(words).most_common(5)
print(most_five_words)

print(Counter('abcdeabcadeaeeeessfa').most_common(3))
print(Counter('abcdeabcadeaeeeessfa 1 2 1 2 2 3 3').most_common(3))
print(Counter('abcdeabcadeaeeeessfa 1').most_common(3))


