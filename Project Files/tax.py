
P = int(input("Principal Amount: "))
r = float(input("Interest rate in percent: "))/100
t = int(input("Investment Period in year(s): "))
n = int(input("Times compounded in a year: "))

amtReturn = P*(1+(r/n))**(n*t)
amtReturn = round(amtReturn, 2)

print("\nThe return amount in " + str(t) + " years is: " + str(amtReturn))

print(input("\nPress Enter to Continue"))
'''10

# List Slicing Syntax

lss = range(0, 101)
print(list(lss[0::4]))
'''
