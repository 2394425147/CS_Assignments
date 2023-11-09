import math
def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    if number == 2 or number == 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    evaluator = 5
    number_sqrt = math.sqrt(number)

    while evaluator <= number_sqrt:
        if number % evaluator == 0 or number % (evaluator + 2) == 0:
            return False
        
        evaluator += 6

    return True

while True:
    number = int(input("请输入一个大于0的整数: "))

    if number == 0:
        break

    if is_prime(number):
        print("是素数")
    else:
        print("不是素数")
