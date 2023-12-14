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
        result_count = len(result)
        if result_count == count and item <= result[-1]:
            continue

        item_added = False
        for i in range(result_count):
            if item > result[i]:
                result.insert(i, item)
                item_added = True
                break

        # Only happens if the list isn't full
        if not item_added:
            result.append(item)

        # At this point a new item is guaranteed to have been added
        # So if the loop started with a full list,
        # there's surely an extra item at the end
        if result_count == count:
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
