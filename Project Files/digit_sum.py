
def digit_sum(x):
    total = 0
    digits = str(x)
    #print(digits)
    for n in digits:
        number = int(n)
        total += number
    return print("\nThe sum of the numbers is "+ str(total) + "\n")

print("\nThis program calculates the sum of all digits of an integer number.\n")
digit_sum(str(input("Insert a Number: \n")))

print(input("--Press Enter to End--"))

