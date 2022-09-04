'''
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(a):
    v = len(a)
    if v%2==0:
        return ""
    else:
        n = int((v-1)/2)
        return a[n]
    
print (mid("aaabaaa"))