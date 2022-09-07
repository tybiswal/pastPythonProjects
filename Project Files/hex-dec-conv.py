# hex-dec converter

hexEq = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15"
}


def hex2dec(hexInput):
    hexInput = hexInput.upper()
    code = [list(hexInput[0]) + list(hexInput[1]), list(hexInput[2]) + list(hexInput[3]),
            list(hexInput[4]) + list(hexInput[5])]
    result = []
    for x in code:
        nsum = 0
        a = (int(str(hexEq[x[0]]))) * 16
        b = int(str(hexEq[x[1]]))
        nsum += a + b
        result.append(a + b)
    return print("\nThe RGB Code is as follows:\n" + str(list(result)))


print("\n>>>     Hexadecimal to Decimal Converter     <<<\n")

while True:
    inCode = input("Input the hex code: #")
    if len(inCode) == 6:
        hex2dec(inCode)
        print(input("Press Enter to Continue..."))
        break
    else:
        print("The code entered is incorrect. Please try again.\n")
        continue
