def print_diamond(height: int):
    row = 1
    while row < height:
        print(" " * (height - row) + "*" * (2 * row - 1))
        row += 1
    while row >= 1:
        print(" " * (height - row) + "*" * (2 * row - 1))
        row -= 1
    pass

number = int(input("N: "))
print_diamond(number)
