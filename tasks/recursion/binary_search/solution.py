def binary_search(arr: list[int], target: int) -> int:
    """Функция классического бинарного поиска по
    отсортированному по возрастанию массиву целых чисел.
    :param arr: отсортированный массив
    :param target: целевое значение
    :return: индекс целевого значения, либо -1, если такого элемента нет
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        middle_elem = (start + end) // 2
        if arr[middle_elem] == target:
            return middle_elem

        if target < arr[middle_elem]:
            end = middle_elem - 1
        else:
            start = middle_elem + 1

    return -1
