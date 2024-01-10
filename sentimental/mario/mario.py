from cs50 import get_int

hash = "#"

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

for i in range(1, height + 1):
    rev = height - i
    print(" " * rev, end="""#""" * i)
    print("""""")




