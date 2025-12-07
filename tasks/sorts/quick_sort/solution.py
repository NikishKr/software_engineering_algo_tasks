def quick_sort(arr: list[int]) -> list[int]:
    """Функция для быстой сортировки
    массива целых чисел по возрастанию.
    """
    if len(arr) < 2:
        return arr.copy()

    def quick_sort_recursion(array: list[int], left: int, right: int) -> None:
        if left >= right:
            return

        pivot = array[left]
        current_index = left + 1
        for i in range(left + 1, right + 1):
            if array[i] < pivot:
                array[i], array[current_index] = array[current_index], array[i]
                current_index += 1

        array[left], array[current_index - 1] = array[current_index - 1], array[left]
        quick_sort_recursion(array, left, current_index - 2)
        quick_sort_recursion(array, current_index, right)

    arr_copy = arr.copy()
    quick_sort_recursion(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy
