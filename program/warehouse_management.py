#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit):
    """Алгоритм поиска с ограничением по глубине."""
    if node is None:
        return False

    # Если нашли целевой узел
    if node.value == goal:
        return True

    # Если достигнут лимит по глубине
    if limit == 0:
        return False

    # Рекурсивный поиск по левой и правой ветке с уменьшением лимита
    return depth_limited_search(
        node.left, goal, limit - 1
    ) or depth_limited_search(node.right, goal, limit - 1)


if __name__ == "__main__":
    # Структура дерева
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None),
    )

    goal = 4
    limit = 2

    # Поиск с ограничением глубины
    found = depth_limited_search(root, goal, limit)

    if found:
        print(f"Цель найдена: <{goal}>")
    else:
        print("Цель не найдена в пределах ограниченной глубины.")
