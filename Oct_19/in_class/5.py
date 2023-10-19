n = input("请输入一个正整数：")

if not n.isnumeric() or int(n) <= 0:
    print(f"请确认 {n} 是一个大于 0 的正整数")

n = int(n)
print(sum(range(1, n + 1)))