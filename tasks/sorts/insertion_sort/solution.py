def insertion_sort(arr: list[int]) -> list[int]:
    """Функция для сортировки вставками
    массива целых чисел.
    """
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element

    return arr
