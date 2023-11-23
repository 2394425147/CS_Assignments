def decompose(num: int) -> [int]:
    """
    Decomposes a number into a list of its components

    Parameters:
    num (int): The number to decompose

    Returns:
    A list of num's components
    """
    import math
    components = [1]

    num_sqrt = math.sqrt(num)
    for i in range(2, int(num_sqrt) + 1):
        if num % i != 0:
            continue

        components.append(i)
        components.append(num // i)
    
    components.sort()
    return components


while True:
    rawNumber = input("请输入一个数字 (输入0结束): ")
    if not rawNumber.isdigit():
        print("输入的不是数字，请重新输入")
        continue
    number = int(rawNumber)
    if number == 0:
        break
    print(decompose(number))
