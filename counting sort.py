#!/usr/bin/env python
#
# This makes use of a cool property of histograms: that they can be used to find the index of placement.
#
# {1, 0, 3, 1, 3, 1}
#
# has histogram:
#
# 0: 1
# 1: 3
# 2: 0
# 3: 2
#
# accumulating those frequencies:
#   [1,3,0,2] -> [1,4,4,6]
# and shifting to the right:
#   [1,4,4,6] -> [0,1,4,4] gives a lookup of where histogram element i will be placed, ie:
#
# element 0 will be placed at lookup[0]==0
# element 1 will be placed at lookup[1]==1
# element 2 will be placed at lookup[2]==4
# element 3 will be placed at lookup[3]==4
# 

import random
import itertools

def counting_sort(x):
    histogram = [0]*(max(x)+1)
    for value in x:
        histogram[value] += 1

    # lookup is the prefix sum of the histogram
    lookup = list(itertools.accumulate(histogram))

    # shift to the right
    lookup = [0] + lookup[0:-1]

    result = [None]*len(histogram)

    for value in x:
        idx = lookup[value]
        result[idx] = value
        lookup[value] += 1

    return result

foo = list(range(100))
random.shuffle(foo)
print(foo)

bar = counting_sort(foo)
print(bar)
