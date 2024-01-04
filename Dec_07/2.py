def init_data(arr: list[int], n: int):
    """
    Populates an array with stub data

    Parameters:
    arr: The array to be populated
    n: The number of elements to add to the array
    """
    import random
    arr.clear()
    arr.extend([random.randint(40, 100) for _ in range(n)])
    pass


def print_data(arr: list[int]):
    """
    Prints the elements of the array

    Parameters:
    arr: The array to be printed
    """
    index = 0
    while index < len(arr):
        if index % 10 == 0:
            print()
        print(arr[index], end=" ")
        index += 1
    print()
    pass


def bubble_sort(arr: list[int]):
    """
    Sorts the elements of the array in ascending order

    Parameters:
    arr: The array to be sorted
    """
    for start in range(len(arr) - 1): # We don't need to sort after the second to last element
        for comp in range(start + 1, len(arr)):
            if arr[start] > arr[comp]:
                arr[start], arr[comp] = arr[comp], arr[start]
    pass


def main():
    arr = []
    count = int(input("请输入考生数："))
    init_data(arr, count)
    print("初始化分数：")
    print_data(arr)
    
    bubble_sort(arr)
    print("排序后：")
    print_data(arr)
    pass


if __name__ == "__main__":
    main()
