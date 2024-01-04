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


def selection_sort(arr: list[int]):
    """
    Sorts the elements of the array in ascending order

    Parameters:
    arr: The array to be sorted
    """
    first_unsorted = 0
    array_length = len(arr)
    while first_unsorted < array_length - 1: # We don't need to sort after the second to last element
        min_index = first_unsorted
        for i in range(first_unsorted + 1, array_length):
            if arr[i] < arr[min_index]:
                min_index = i
        
        arr[first_unsorted], arr[min_index] = arr[min_index], arr[first_unsorted]
        first_unsorted += 1
    pass


def main():
    arr = []
    count = int(input("请输入考生数："))
    init_data(arr, count)
    print("初始化分数：")
    print_data(arr)
    
    selection_sort(arr)
    print("排序后：")
    print_data(arr)
    pass


if __name__ == "__main__":
    main()
