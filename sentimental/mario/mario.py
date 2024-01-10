from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for i in range(height, -1, -1):
    for j in range(0, height):
        print(" ")
    print("#" * i, end="\n")
