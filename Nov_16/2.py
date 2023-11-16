def GCD_function(number1: int, number2: int) -> (int, int):
    # calculate gcd
    swizzle1 = number1
    swizzle2 = number2
    while(swizzle2):
        swizzle1, swizzle2 = swizzle2, swizzle1 % swizzle2
    gcd = swizzle1
    
    # calculate lcm
    # proof: https://math.stackexchange.com/questions/349858/easiest-and-most-complex-proof-of-gcd-a-b-times-operatornamelcm-a-b-a
    lcm = (number1 * number2) // gcd
    
    return gcd, lcm

while True:
    number1 = int(input("请输入第一个数字(输入0结束): "))
    if number1 == 0:
        break

    number2 = int(input("请输入第二个数字(输入0结束): "))
    if number2 == 0:
        break

    gcd, lcm = GCD_function(number1, number2)
    print(f"最大公约数: {gcd}\n最小公倍数: {lcm}\n")
