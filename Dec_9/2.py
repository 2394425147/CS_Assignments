def print_equilateral(height: int):
    row = 1
    while row <= height:
        print(" " * (height - row) + "*" * (2 * row - 1))
        row += 1
    pass

number = int(input("Height: "))
print_equilateral(number)
