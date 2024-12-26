#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Problem:
    """Абстрактный класс задачи поиска пути."""

    def __init__(self, initial=None, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Возвращает допустимые действия для состояния."""
        raise NotImplementedError

    def result(self, state, action):
        """Возвращает новое состояние после выполнения действия."""
        raise NotImplementedError

    def is_goal(self, state):
        """Проверяет, является ли состояние целевым."""
        return state == self.goal

    def action_cost(self, s, a, s1):
        """Возвращает стоимость действия."""
        return 1


class Node:
    """Класс, представляющий узел в дереве поиска."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return f"<Node {self.state}>"

    def path(self):
        """Возвращает путь от начального узла до текущего."""
        node, path = self, []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]


class ItalyGraphProblem(Problem):
    """Задача поиска пути между городами в Италии."""

    def __init__(self, graph, initial, goal):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, state):
        """Возвращает соседние города (действия)."""
        return self.graph.get(state, {}).keys()

    def result(self, state, action):
        """Возвращает город, в который совершается переход."""
        return action

    def action_cost(self, s, a, s1):
        """Возвращает стоимость перехода между двумя городами."""
        return self.graph[s][s1]


def depth_limited_search(problem, limit):
    """
    Реализация поиска с ограничением глубины.
    Возвращает путь и стоимость, если решение найдено, иначе None.
    """

    def recursive_dls(node, problem, limit):
        if problem.is_goal(node.state):
            return node

        if limit == 0:
            return None

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            child_cost = node.path_cost + problem.action_cost(
                node.state, action, child_state
            )
            child_node = Node(child_state, node, action, child_cost)

            result = recursive_dls(child_node, problem, limit - 1)
            if result:
                return result

        return None

    return recursive_dls(Node(problem.initial), problem, limit)


def find_solution_with_dls(graph, start, goal, depth_limit):
    """Ищет минимальный путь с использованием DLS."""
    problem = ItalyGraphProblem(graph, start, goal)
    for depth in range(1, depth_limit + 1):
        solution = depth_limited_search(problem, depth)
        if solution:
            return solution, depth
    return None, None


def main():
    """Основная функция для поиска пути с ограничением глубины."""
    graph = {
        "Турин": {
            "Иврея": 51,
            "Новара": 95,
            "Милан": 140,
            "Асти": 56,
            "Кунео": 98,
        },
        "Иврея": {"Турин": 51, "Биелла": 25},
        "Биелла": {"Иврея": 25, "Верчелли": 43},
        "Новара": {"Турин": 95, "Милан": 52, "Генуя": 151, "Павия": 42},
        "Верчелли": {"Биелла": 43, "Алессандрия": 57},
        "Варезе": {"Милан": 60, "Павия": 94},
        "Милан": {
            "Турин": 140,
            "Новара": 52,
            "Варезе": 60,
            "Бергамо": 60,
            "Брешиа": 91,
            "Кремона": 91,
            "Пьяченца": 69,
            "Генуя": 52,
            "Павия": 42,
        },
        "Бергамо": {"Милан": 60, "Брешиа": 51},
        "Брешиа": {"Милан": 91, "Верона": 73, "Кремона": 58, "Бергамо": 51},
        "Верона": {"Брешиа": 73, "Модена": 105},
        "Кремона": {"Брешиа": 58, "Милан": 96, "Павия": 77},
        "Пьяченца": {"Милан": 69, "Парма": 74, "Генуя": 144},
        "Парма": {"Пьяченца": 74, "Реджо-Эмилия": 28},
        "Реджо-Эмилия": {"Парма": 28, "Модена": 25},
        "Модена": {"Верона": 105, "Реджо-Эмилия": 25},
        "Генуя": {"Новара": 151, "Пьяченца": 144, "Милан": 161},
        "Алессандрия": {"Верчелли": 57, "Асти": 38},
        "Асти": {"Турин": 56, "Алессандрия": 38, "Кунео": 104},
        "Кунео": {"Турин": 98, "Асти": 104},
        "Павия": {"Варезе": 94, "Милан": 42, "Кремона": 77},
    }

    start = "Алессандрия"
    goal = "Милан"
    depth_limit = 10

    solution, depth = find_solution_with_dls(graph, start, goal, depth_limit)

    if solution:
        print("Путь:", solution.path())
        print("Стоимость:", solution.path_cost)
        print("Найдено на глубине:", depth)
    else:
        print("Решение не найдено в пределах заданной глубины.")


if __name__ == "__main__":
    main()
