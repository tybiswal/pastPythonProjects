'''
Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
Your code should find the biggest number of consecutive zeros in the string.
 For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. 
Your function should return the number described above.
'''

def consecutive_zeros(a):
    a.split("1",-1)
    t = max(a)
    return len(t)

'''
x = "1001101000110"
v = x.split("1",-1)
t = max(v)
print(len(t))
'''

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])