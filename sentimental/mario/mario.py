from cs50 import get_int

hash = "#"

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for i in range(1, height):
    rev = height - i
    print("\n")
    print(" " * rev, end="#" * i)




