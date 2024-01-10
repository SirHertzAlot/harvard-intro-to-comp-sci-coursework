from cs50 import get_string

digit = 0
sum = 0

strcc = get_string("card number: ")

cc = list(strcc)

ccid = append.

for i in range(0, len(cc)):

    digit = int(cc[i]);

    if i % 2 == 0:

        digit *= 2;

        if digit > 9:

            digit -= 9

    sum += digit

if sum % 10 == 0:
    if cc[0] == 3 and cc[1] == 4 or cc[0] == 3 and cc[1] == 7:
        print("AMEX\n")
    elif cc[0] == 5 and cc[1] == 1 or cc[0] == 5 and cc[1] == 2 or cc[0] == 5 and cc[1] == 4 or cc[0] == 5 and cc[1] == 5:
        print("MASTERCARD\n")
    elif cc[0] == 4:
        print("VISA\n")
    else:
        print("INVALID\n")
else:
    print("INVALID\n")
