def print_diamond(height: int):
    for row in range(height - 1, -height, -1):
        print(" " * abs(row), "*" * ((height - abs(row)) * 2 - 1), sep="")

number = int(input("N: "))
print_diamond(number)
