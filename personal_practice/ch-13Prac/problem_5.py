from functools import reduce
a = [111, 2, 45, 54, 564, 54634, 56]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))