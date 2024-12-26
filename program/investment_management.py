#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def find_max_at_depth(node, depth, limit):
    if node is None or depth > limit:
        return float("-inf")

    if depth == limit:
        return node.value

    left_max = find_max_at_depth(node.left, depth + 1, limit)
    right_max = find_max_at_depth(node.right, depth + 1, limit)

    return max(left_max, right_max)


if __name__ == "__main__":
    root = BinaryTreeNode(
        3,
        BinaryTreeNode(1, BinaryTreeNode(0), None),
        BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
    )

    limit = 2
    max_value = find_max_at_depth(root, 0, limit)
    print(f"Максимальное значение на указанной глубине: {max_value}")
