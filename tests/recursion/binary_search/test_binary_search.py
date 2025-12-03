from tasks.recursion.binary_search.solution import binary_search


def test_empty():
    arr = []
    assert binary_search(arr, 0) == -1


def test_one_element():
    arr = [3]
    assert binary_search(arr, 3) == 0
    assert binary_search(arr, 9) == -1


def test_usual():
    arr = [1, 2, 2, 4, 7, 7, 7, 9, 17]
    assert binary_search(arr, 7) in (4, 5, 6)
    assert binary_search(arr, 2) in (1, 2)
    assert binary_search(arr, 9) == 7


def test_no_target():
    arr = [1, 2, 2, 4, 7, 9]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 5) == -1
    assert binary_search(arr, 10) == -1


def test_negative():
    arr = [-5, -3, -2, -2, -1]
    assert binary_search(arr, -2) in (2, 3)
    assert binary_search(arr, -3) == 1


def test_boundary():
    arr = [0, 3, 10, 38]
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 38) == 3


def test_large_array():
    arr = list(range(1000000))
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 345678) == 345678
    assert binary_search(arr, 999999) == 999999
    assert binary_search(arr, 1000000) == -1
