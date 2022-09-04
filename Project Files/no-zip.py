'''
Custom zip

The built-in zip function "zips" two lists. Write your own implementation of this function.

Define a function named zap. The function takes two parameters, a and b. These are lists.

Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.

You may assume a and b have equal lengths.

If you don't get it, think of a zipper.

For example:

zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)

Should return:

[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)]
'''

def zap(a,b):
    x = []
    for i in range(0, len(a)):
        q = (a[i], b[i])
        x.append(q)
        i+=1
    return x    
    

print(zap(
    [0, 1, 2, 3,5,6,7,8,9,0],
    [5, 6, 7, 8,5,1,3,1,4,5]
))