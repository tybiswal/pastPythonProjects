'''
Flatten a list

Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. 
It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])

Should return the list:

[1, 2, 3, 4]

'''

def flatten(a):
    b=[]
    for i in a:
        for j in i:
            b.append(j)
    return b
        
t = flatten([[2,1],[3,4]])

print(t)
