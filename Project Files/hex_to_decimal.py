# hex_to_decimal rgb colors

hexvar = str(input('Input the Hex Number of the Color: #'))

reds = (hexvar[0]+hexvar[1])
blues = (hexvar[2]+hexvar[3])
greens = (hexvar[4]+hexvar[5])

print('The color in RGB is ' + '(' + str(int(reds, 16)) + ', ' + str(int(blues, 16)) + ', ' + str(int(greens, 16)) + ')')