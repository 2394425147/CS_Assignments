def min_max(arr: [int]) -> (int, int):
    """
    Gets the max value and the min value of an input array

    Parameters:
    arr: The target list of integers

    Returns:
    Two numbers, the first being the min value and the second being the max.
    """
    min = max = arr[0]
    for number in arr:
        if number < min:
            min = number
        if number > max:
            max = number
    return min, max


def init_data(arr: [int], n: int):
    """
    Populates an array with random integers ranged [1, 1000]

    Parameters:
    arr: The array to be filled with data
    n: Size of the populated array
    """
    import random
    arr = [random.randint(1, 1000) for _ in range(n)]

def main():
    n = 1000
    arr = []
    init_data(arr, n)
    min_val, max_val = min_max(arr)
    print(f"Min: {min_val}, Max: {max_val}")


if __name__ == "__main__":
    main()
