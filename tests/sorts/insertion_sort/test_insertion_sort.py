import pytest

from tasks.sorts.insertion_sort.solution import insertion_sort


def test_empty():
    assert insertion_sort([]) == []


def test_one_element():
    assert insertion_sort([7]) == [7]


def test_usual():
    assert insertion_sort([9, 5, 1, 4, 3, 2, 6]) == [1, 2, 3, 4, 5, 6, 9]


def test_sorted_array():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_array():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_negative_and_repetition():
    assert insertion_sort([2, -3, -1, 2, -1, 4, 0, -4, -4]) == [-4, -4, -3, -1, -1, 0, 2, 2, 4]
