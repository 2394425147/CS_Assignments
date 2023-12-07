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


def find_insertion_index(arr: list[int], value: int, start: int, end: int) -> int:
    """
    Finds the index where a value should be inserted in a sorted array to maintain the sorted order

    Parameters:
    arr: The array in which to find the insertion index
    value: The value to be inserted
    start: The starting index of the search range
    end: The ending index of the search range

    Returns:
    The index where the value should be inserted
    """
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

    return start


def insertion_sort(arr: list[int]):
    """
    Sorts the elements of the array in ascending order

    Parameters:
    arr: The array to be sorted
    """
    for i in range(1, len(arr)):
        key = arr[i]
        insertion_index = find_insertion_index(arr, key, 0, i - 1)
        for j in range(i - 1, insertion_index - 1, -1):
            arr[j + 1] = arr[j]
        
        arr[insertion_index] = key
    pass


def main():
    arr = []
    count = int(input("请输入考生数："))
    init_data(arr, count)
    print("初始化分数：")
    print_data(arr)
    
    insertion_sort(arr)
    print("排序后：")
    print_data(arr)
    pass


if __name__ == "__main__":
    main()
