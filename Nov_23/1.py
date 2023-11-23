def is_narcissistic(num: str) -> bool:
    """
    Checks if a number is a narcissistic number
    A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits

    Parameters:
    num (str): The number to check.

    Returns:
    True if the number is narcissistic, False otherwise.
    """
    num_length = len(num)
    return num == sum(int(x) ** num_length for x in str(num))

while True:
    rawNumber = input("请输入一个[100~999]之间的数字：")
    if not rawNumber.isdigit():
        print("输入的不是数字，请重新输入")
        continue
    number = int(rawNumber)
    if number < 100 or number > 999:
        print("输入的数字不在[100, 999]范围内，程序结束")
        break
    print(rawNumber,"不是" if is_narcissistic(rawNumber) else "为", "水仙花数", sep="")
