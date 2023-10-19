def is_number(number: any):
    return isinstance(number, (float, int))

total = 0
for _ in range(5):
    number = input("输入数字：")
    if not is_number(number):
        print("请确认您输入的是数字")
        exit(-1)
    total += int(number)

print(f"平均值：{total / 5}")
