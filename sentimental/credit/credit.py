from cs50 import get_string

digit = 0
strcc = 0
sum = 0
ccid = []

strcc = get_string("card number: ")

cc = list(strcc)

for i in range(0, len(cc)):

    ccid.append(cc[0:2])

    if i % 2 == 0:

        digit = int(cc[i]) * 2

        if digit > 9:

            digit -= 9

    sum += digit



if sum % 10 == 0:
    if ccid == 34 or ccid == 37:
        print("AMEX\n")
    elif ccid == 51 or ccid == 52 or ccid == 53 or ccid == 54 or ccid == 55:
        print("MASTERCARD\n")
    elif ccid[0] == 4:
        print("VISA\n")
    else:
        print("INVALID\n")
else:
    print("INVALID\n")
