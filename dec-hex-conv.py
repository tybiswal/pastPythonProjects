hex_eq = {
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
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F"
}
def hexConv(codes):
    hexNames = "#"
    for data in codes:
        if data > 16:
            n = str(data // 16)
            r = str(int(((data / 16) - int(n))*16))
            hexNames += str(hex_eq[n])+str(hex_eq[r])

        else:
            hexNames += str(hex_eq['0'])+str(hex_eq[str(data)])
    return hexNames

def runApp():
    print("\nRGB to HEX Converter Tool\n"+"Works Flawlessly!\n"+"Insert The Numbers Below\n")
    while True:
        r_code = int(input("What is the number for Red Channel?: "))
        g_code = int(input("What is the number for Green Channel?: "))
        b_code = int(input("What is the number for Blue Channel?: "))
        if r_code < 256 and g_code < 256 and b_code < 256:
            rgb_codes = [r_code, g_code, b_code]
            print("\n>>>     The HEX code is: "+ str(hexConv(rgb_codes))+"     <<<\n\nThank you!")
            print(input("\nPress Enter to Continue ..."))
            break
        else:
            print("\nError: Please enter valid input: Values for R, G and B should be from 0 to 255 only!\n")
            continue
    return

runApp()