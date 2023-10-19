import sanitization

# Implementation
def identify(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    pass

# Testing
while True:
    (shouldContinue, number) = sanitization.filter_integer(input("请输入正整数："))

    if not shouldContinue:
        break;

    identify(number)
    pass
