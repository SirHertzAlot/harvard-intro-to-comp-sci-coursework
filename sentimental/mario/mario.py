from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0:
        break

for i in range(0, height + 1):
    print('#' * i)
print()
