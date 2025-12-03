import pytest

from tasks.data_stuctures.stack_max.solution import StackMax


def test_usual():
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    stack.push(7)
    assert stack.get_max() == 7

    stack.push(1)
    stack.push(3)
    assert stack.get_max() == 7

    stack.pop()
    stack.pop()
    assert stack.get_max() == 7

    stack.pop()
    assert stack.get_max() == "None"


def test_many_push():
    stack = StackMax()

    stack.push(2)
    stack.push(-8)
    stack.push(9)
    stack.push(-100)
    stack.push(15)
    assert stack.get_max() == 15

    stack.pop()
    assert stack.get_max() == 9

    stack.pop()
    stack.pop()
    assert stack.get_max() == 2

    stack.pop()
    stack.pop()
    assert stack.pop() == "error"


def test_many_pop():
    stack = StackMax()
    assert stack.pop() == "error"

    stack.push(9999)
    stack.push(789)
    assert stack.get_max() == 9999

    stack.pop()
    stack.pop()
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    assert stack.pop() == "error"


def test_identical_max():
    stack = StackMax()
    assert stack.get_max() == "None"

    stack.push(52)
    stack.push(52)
    stack.push(52)
    assert stack.get_max() == 52

    stack.pop()
    assert stack.get_max() == 52

    stack.pop()
    stack.pop()
    assert stack.get_max() == "None"


def test_cycles():
    stack = StackMax()
    for i in range(10000):
        stack.push(i)
        assert stack.get_max() == i

    for i in range(5000):
        stack.pop()
        assert stack.get_max() == 9998 - i
