from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for i in reversed(range(0, height)):
    print("#" * i, end=" ")
