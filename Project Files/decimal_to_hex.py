# converts decimal to hex manually

import math

decnum = int(input('Please enter an integer number: '))

hexarray = []

while decnum > 0:
    remainder = decnum%16
    if remainder == 10:
        remainder = 'A'
    elif remainder == 11:
        remainder = 'B'
    elif remainder == 12:
        remainder = 'C'
    elif remainder == 13:
        remainder = 'D'
    elif remainder == 14:
        remainder = 'E'
    elif remainder == 15:
        remainder = 'F'
    hexarray.append(remainder)
    decnum = math.floor(decnum/16)

hexcode = ''

n = len(hexarray)
while n > 0:
    hexcode+=str((hexarray[n-1]))
    n-=1

print(hexcode)
