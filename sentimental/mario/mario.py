from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for i in range(0, height):
    print("#" * i, end="\n")
    for j in range(height, -1, -1):
        print(" ")
