def get_fibonacci_value(num: int) -> int:
    """
    This function calculates the Fibonacci value of a given number

    Parameters:
    num (int): The index of the number you'd like to find in the fibonacci sequence

    Returns:
    int: The Fibonacci value of the given number
    """
    if num == 0:
        return 0
    if num == 1:
        return 1

    mem = [0, 1]
    index = 1
    while index != num:
        mem[0], mem[1] = mem[1], mem[0] + mem[1]
        index += 1
    
    return mem[1]

while True:
    rawNumber = input("请输入一个数字 (输入0结束): ")
    if not rawNumber.removeprefix("-").isdigit():
        print("输入的不是数字，请重新输入")
        continue
    number = int(rawNumber)
    if number < 0:
        break
    print(get_fibonacci_value(number))