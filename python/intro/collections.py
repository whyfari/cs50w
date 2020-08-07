#!/usr/bin/python3.7
from collections import Counter
from collections import defaultdict
from collections import namedtuple

# COUNTER
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.


myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
print(Counter(myList))
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

print(Counter(myList).items())
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

print(Counter(myList).keys())
#[1, 2, 3, 4, 5]

# DEFAULT DICTIONARY
# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.


# DEFAULT DICTIONARY
# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)

# Basically, namedtuples are easy to create, lightweight object types. They turn tuples into convenient containers for simple tasks. With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
Point = namedtuple('Point', 'x,y')
pt1 = Point(1, 2)
pt2 = Point(3, 4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot_product)
