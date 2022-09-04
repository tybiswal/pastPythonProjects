'''
n = 5

array = []

i = 0
while i < n:
    array.append(i)
    i+=1

print (array)

x = 0
for x in array:
    y=array[x]
    print (y*y)
    x+=1

def is_leap(year):
    leap = False
    
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(2100)

print(is_leap(year))

n = 6

i = 1
while i < n:
    print (i, sep='')
    i+=1
'''

x = 2
y = 2
z = 2
n = 2

big =[]
small =[]
i = 0