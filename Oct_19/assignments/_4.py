for col in range(9):
    for row in range(col + 1):
        print(f"{col + 1}*{row + 1}={(col + 1) * (row + 1)}", end="\t")
    print()