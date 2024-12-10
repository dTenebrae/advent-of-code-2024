import numpy as np


class Node:
    def __init__(self, level: int, children: list, coordinates=None):
        self.level = level
        self.children = children
        self.coordinates = coordinates


class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: list(map(int, list(x.strip()))), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return np.array(data)

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        self.global_cnt = 0

    # def print_tree(self, tree: Node):
    #     print(f"level:{tree.level} - {tree.coordinates}")
    #     if not tree.children:
    #         return
    #     for child in tree.children:
    #         return self.print_tree(child)

    def print_tree(self, root: Node, marker_str="+- ", level_markers=None):
        if level_markers is None:
            level_markers = []
        empty_str = " " * len(marker_str)
        connection_str = "|" + empty_str[:-1]
        level = len(level_markers)
        mapper = lambda draw: connection_str if draw else empty_str
        markers = "".join(map(mapper, level_markers[:-1]))
        markers += marker_str if level > 0 else ""
        print(f"{markers}({root.coordinates[0]}, {root.coordinates[1]})")
        for i, child in enumerate(root.children):
            is_last = i == len(root.children) - 1
            self.print_tree(child, marker_str, [*level_markers, not is_last])

    def get_starts(self):
        return zip(*np.where(self.data == 0))

    def create_forest(self):
        forest = []
        start_points = self.get_starts()

        for start_x, start_y in start_points:
            current_weight = 0
            tree = Node(level=current_weight, children=[], coordinates=(start_x, start_y))
            forest.append(tree)
            self.grow_tree(tree)

        return forest

    def is_valid(self, x, y, weight):
        return (0 <= x < self.data.shape[0] and 0 <= y < self.data.shape[1]
                and self.data[x, y] == weight)

    def grow_tree(self, leaf):
        if leaf.level == 9:
            self.global_cnt += 1
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        x, y = leaf.coordinates
        test_weight = leaf.level + 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny, test_weight):
                if int(nx) == 2 and int(ny) == 2:
                    print()
                leaf.children.append(Node(level=test_weight, children=[], coordinates=(nx, ny)))

        for child in leaf.children:
            return self.grow_tree(child)


if __name__ == '__main__':
    sol = Solution("../test.txt")
    sol.create_forest()
    print(sol.global_cnt)
