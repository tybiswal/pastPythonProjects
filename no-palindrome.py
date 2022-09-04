'''
Palindrome

A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.
'''

def palindrome(word):
    rev =""
    a = []
    for x in word:
        a.insert(0,x)
    for y in a:
        rev +=y
    return word == rev

# smarter solution:
# check if reversing the string gives the same string.
def palindrome2(string):
    return string == string[::-1]

print(palindrome2("radar"))