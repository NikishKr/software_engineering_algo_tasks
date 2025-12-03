from tasks.sorts.quick_sort.solution import quick_sort


def test_empty():
    assert quick_sort([]) == []


def test_one_element():
    assert quick_sort([3]) == [3]


def test_usual():
    assert quick_sort([3, 7, 9, 4, 3, 1, 8, 5]) == [1, 3, 3, 4, 5, 7, 8, 9]


def test_sorted_array():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_array():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_negative_and_repetition():
    assert quick_sort([2, -3, -1, 2, -1, 4, 0, -4, -4]) == [-4, -4, -3, -1, -1, 0, 2, 2, 4]


def test_identical_elements():
    assert quick_sort([3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3]
