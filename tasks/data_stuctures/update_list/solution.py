from typing import Optional


class Node:
    def __init__(self, value: str, next_item: Optional["Node"] = None) -> None:
        self.value = value
        self.next_item = next_item


def solution(node: Node, idx: int) -> Optional[Node]:
    """Функция, удаляющая элемент из
    односвязного списка по заданному индексу.

    :param node: голова списка
    :param idx: индекс удаляемого элемента
    :return: голова обновлённого списка
    """
    current_elem: Optional[Node] = node
    current_idx = 0

    if idx == 0 and node.next_item is not None:
        return node.next_item

    while current_elem is not None and current_idx < idx - 1:
        current_idx += 1
        current_elem = current_elem.next_item

    if current_elem is not None and current_elem.next_item is not None:
        current_elem.next_item = current_elem.next_item.next_item

    return node
