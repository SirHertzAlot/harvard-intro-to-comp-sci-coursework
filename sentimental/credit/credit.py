from cs50 import get_string

digit = 0
strcc = 0
sum = 0
ccid = []

strcc = get_string("card number: ")

cc = list(strcc)

ccid.append(cc[0:2])

for i in range(0, len(cc)):

    ogdigit = int(cc[i]);

    if i % 2 == 0:

        digit = ogdigit * 2;

        if digit > 9:

            digit -= 9

    sum += digit

if sum % 10 == 0:
    if ccid[0] == 3 and ccid[1] == 4 or ccid[0] == 3 and ccid[1] == 7:
        print("AMEX\n")
    elif ccid == 51 or ccid == 52 or ccid == 53 or ccid == 54 or ccid == 55:
        print("MASTERCARD\n")
    elif ccid[0] == 4:
        print("VISA\n")
    else:
        print("INVALID\n")
else:
    print("INVALID\n")
