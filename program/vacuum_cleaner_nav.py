#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    """Класс, представляющий узел двоичного дерева."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit):
    """
    Выполняет поиск с ограничением глубины в двоичном дереве.
    Возвращает True, если цель найдена в пределах лимита глубины.
    """

    def recursive_dls(current_node, current_depth):
        if current_node is None:
            return False

        if current_node.value == goal:
            return True

        if current_depth >= limit:
            return False

        # Проверяем левое и правое поддеревья
        return recursive_dls(
            current_node.left, current_depth + 1
        ) or recursive_dls(current_node.right, current_depth + 1)

    return recursive_dls(node, 0)


def main():
    """Основная функция для тестирования алгоритма."""
    # Дерево комнат
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None),
    )
    goal = 4
    limit = 1

    found = depth_limited_search(root, goal, limit)

    if found:
        print("Найден на глубине:", True)
    else:
        print("Целевая комната не найдена в пределах лимита глубины.")


if __name__ == "__main__":
    main()
