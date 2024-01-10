from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for j in range(1, height):
    print(" ")
    for i in range(1, height):
        print("#" * i, end="\n")



