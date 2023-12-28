def main():
    with open(__file__, "r") as f:
        lines = f.readlines()
        line_count = len(lines)
        line_count_width = len(str(line_count))
        for index, line in enumerate(lines):
            print(f"{index + 1:>{line_count_width}} | {line}", end="")
    pass

if __name__ == "__main__":
    main()