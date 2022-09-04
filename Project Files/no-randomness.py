'''
Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.

from random import choice

def random_number():
    b=[]
    for i in range(1,101):
        b.append(i)
        i+=1
    return print(choice(b))

random_number()
'''
from random import randint
print(randint(1,101))

