from cs50 import get_string

digit = 0
sum = 0
ccid = []

strcc = get_string("card number: ")

cc = list(strcc)

ccid.insert(0, cc[0])
ccid.insert(1, cc[1])

for i in range(0, len(cc)):

    digit = int(cc[i]);

    if i % 2 == 0:

        digit *= 2;

        if digit > 9:

            digit -= 9

    sum += digit

if sum % 10 == 0:
    if ccid[0] == '3' and ccid[1] == '4' or ccid[0] == '3' and ccid[1] == '7':
        print("AMEX\n")
    elif ccid[0] == '5' and ccid[1] == '1' or ccid[0] == '5' and ccid[1] == '2' or ccid[0] == '5' and ccid[1] == '4' or ccid[0] == '5' and ccid[1] == '5':
        print("MASTERCARD\n")
    elif ccid[0] == '4':
        print("VISA\n")
    else:
        print("INVALID\n")
else:
    print("INVALID\n")
