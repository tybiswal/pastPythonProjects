'''
Thousands separator

Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
'''

# My Solution
def format_number(n):
    n = str(n)
    revn = n[::-1]
    c = []
    d = 0
    for i in revn:
        c.append(i)
        d+=1
        if d % 3 == 0:
            c.append(",")
    
    n2 = c[::-1]
    if n2[0] == ",":
        n2.pop(0)
        clean1 = ''.join(n2)
        return clean1
    else: 
        n3 = ''.join(n2)
        return n3


# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)

print(format_number(100333))
