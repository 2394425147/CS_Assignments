import math
def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    evaluator = 2
    number_sqrt = math.sqrt(number)
    while evaluator <= number_sqrt:
        if number % evaluator == 0:
            return False
        
        evaluator += 1

    return True

while True:
    number = int(input("请输入一个大于0的整数: "))

    if number == 0:
        break

    if is_prime(number):
        print("是素数")
    else:
        print("不是素数")
