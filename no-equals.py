'''
All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

# one-liner with nested list comprehension
# and the all() built-in
# all() returns true if its constituents are all True
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)