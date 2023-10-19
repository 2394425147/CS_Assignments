def main():
    data = input("请输入一个0 ~ 900,000,000范围内的整数: ")
    if not data.replace(".", "").replace("-", "").isnumeric():
        print("请确认输入的是一个数字")
        exit(-1)

    if data[0] == "-":
        print("请确认是正整数")
        exit(-1)

    if len(data) > 9 or len(data) == 9 and data[0] == 9 and any(data[1:]):
        print("请确认数字在0 ~ 900,000,000范围内")
        exit(-1)

    total = 0
    for digit in data:
        total += ord(digit) - ord("0")

    print(total)
