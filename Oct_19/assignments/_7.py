import sanitization
import math

# Implementation
def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    sqrt = math.sqrt(number)
    for i in range(2, int(sqrt) + 1):
        if number % i == 0:
            return False
    
    return True

# Testing
while True:
    (shouldContinue, number) = sanitization.filter_integer(input("请输入正整数："))

    if not shouldContinue:
        break;

    print("是素数" if is_prime(number) else "不是素数")
    pass