# Implementation
def identify(number):
    if not isinstance(number, int):
        print(f"{number} is not an integer.")
    elif number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    pass

# Testing
testCases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, "hello"]
for testCase in testCases:
    identify(testCase)
