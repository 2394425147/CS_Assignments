import math

# Implementation
def is_narcissus(number: int) -> bool:
    ones = number % 10
    hundreds = math.floor(number / 100)
    tens = math.floor(number / 10) - hundreds * 10
    return number == ones ** 3 + tens ** 3 + hundreds ** 3

# Testing
testCases = range(100, 1000)
for testCase in testCases:
    if is_narcissus(testCase):
        print(testCase)