def filter_integer(number: str):
    if not number.replace(".", "").replace("-", "").isnumeric():
        print(f"{number} is not a number.")
        return (False, number)
        
    number = eval(number)

    if not isinstance(number, int):
        print(f"{number} is not an integer.")
        return (False, number)

    if number <= 0:
        print(f"{number} is not positive.")
        return (False, number)

    return (True, number)