def get_max(arr: list[int], count: int) -> list[int]:
    """
    Gets the greatest `count` values from a list

    Parameters:
    arr: The array to perform filtering on
    count: How many values to return

    Returns:
    A list of the greatest `count` values from `arr`
    """
    result = []
    for item in arr:
        if len(result) > 0 and item <= result[0]:
            continue
        
        result.insert(0, item)

        if len(result) > count:
            result.pop()

    return result


def init_data(arr: list[int], n: int):
    """
    Populates an array with stub data

    Parameters:
    arr: The array to be populated
    n: The number of elements to add to the array
    """
    import random
    arr.clear()
    arr.extend([random.randint(1, 1000) for _ in range(n)])
    pass


def main():
    arr = []
    count = int(input("请输入填充数字量："))
    init_data(arr, count)
    print("初始化数据：")
    print(arr)

    max_values = get_max(arr, 2)
    print("最大与次大值：")
    print(max_values)
    pass


if __name__ == "__main__":
    main()
