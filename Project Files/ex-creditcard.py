"""
Luhn's algorithm

Assume an example of an account number "7992739871" that will have a check digit added, making it of the form 7992739871x:

    1. From the rightmost digit (excluding the check digit) and moving left, double the value of every second digit.
        The check digit is neither doubled nor included in this calculation;
        the first digit doubled is the digit located immediately left of the check digit.
        If the even_sums of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the even_sums
        (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, equivalently, subtract 9 from the even_sums (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).

    2. Take the sum of all the digits (including the check digit).

    3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula;
        otherwise it is not valid.

"""


def luhn_checksum(n):
    even_sums = ""
    for i, digit in enumerate(str(n)):
        if i != 0 and (i % 2) != 0:
            second_num = str(int(digit) * 2)
            if len(second_num) != 1:
                int_add = int(second_num[0]) + int(second_num[1])
                even_sums += str(int_add)
            else:
                even_sums += second_num
        else:
            even_sums += digit
    summation = 0
    for x in even_sums:
        summation += int(x)
    check_num = (summation * 9) % 10
    return str(n) + str(check_num)


find_checknum = 7992739871
print(luhn_checksum(find_checknum))
