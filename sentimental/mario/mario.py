from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for i in range(height + 1, 0):
    print('#' * i)
