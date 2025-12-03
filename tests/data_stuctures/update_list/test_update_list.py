import pytest

from tasks.data_stuctures.update_list.solution import Node, solution


def test_usual():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


def test_short_list():
    node0 = Node("node0", None)
    new_head = solution(node0, 0)
    assert new_head is node0

    new_head = solution(node0, 1)
    assert new_head.next_item is None

    new_head = solution(node0, 5)
    assert new_head.next_item is None


def test_first_deleting():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    assert new_head is node1

    new_head = solution(new_head, 0)
    assert new_head is node2

    new_head = solution(new_head, 0)
    assert new_head is node3


def test_last_deleting():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 3)
    assert new_head.next_item.next_item.next_item is None

    new_head = solution(new_head, 2)
    assert new_head.next_item.next_item is None

    new_head = solution(new_head, 1)
    assert new_head.next_item is None


def test_different_solutions():
    node5 = Node("node5", None)
    node4 = Node("node4", node5)
    node3 = Node("node3", node4)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 5)
    new_head = solution(new_head, 0)
    new_head = solution(new_head, 2)
    assert new_head is node1
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node4
    assert new_head.next_item.next_item.next_item is None
