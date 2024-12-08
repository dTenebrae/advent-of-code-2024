import numpy as np
from itertools import permutations


class Solution:

    @staticmethod
    def input_open(file_path):

        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: list(map(lambda y: 0 if y == '.' else ord(y), list(x.strip()))), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return np.array(data)

    @staticmethod
    def get_charset(file_path):
        try:
            with open(file_path, "r") as f:
                data = f.read()
                uniq_chars = set(data)
                uniq_chars.remove('.')
                uniq_chars.remove('\n')
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return uniq_chars


    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        self.charset = self.get_charset(file_path)

        print()

    def delta_xy(self, char):
        coords = np.where(self.data == char)
        if not coords or len(coords[0]) == 1:
            return None
        points = [(x, y) for x, y in zip(coords[0], coords[1])]
        for point in permutations(points, 2):
            x1, y1 = point[0]
            x2, y2 = point[1]
            dx = x2 - x1
            dy = y2 - y1
            yield x1, y1, x2, y2, dx, dy


    @staticmethod
    def find_line(x1, y1, x2, y2, dx, dy):
        rows, cols = sol.data.shape
        line_points = []
        x, y = x1, y1
        while 0 <= x < rows and 0 <= y < cols:
            line_points.append((x, y))
            x -= dx
            y -= dy
        x, y = x2, y2
        while 0 <= x < rows and 0 <= y < cols:
            if (x, y) not in line_points:
                line_points.append((x, y))
            x += dx
            y += dy
        return sorted(line_points)

    @staticmethod
    def euc_dist(p1, p2):
        return np.linalg.norm(p1 - p2)

    @staticmethod
    def is_almost_multiple(a, b, epsilon=1e-10) -> bool:
        if b == 0:
            return False
        # Вычисляем ближайшее целое k
        k = round(a / b)
        # Абсолютное отклонение
        delta = abs(a - k * b)
        # Возвращаем результат
        return delta <= epsilon

    def find_antinodes(self, line, start_node, end_node, dist, resonant):
        result = []
        for node in line:
            if not resonant and ((node == start_node).all() or (node == end_node).all()):
                continue
            node_dist = self.euc_dist(node, start_node)
            if resonant:
                if self.is_almost_multiple(node_dist, dist):
                    result.append(node)
                    continue
            if node_dist == dist:
                result.append(node)
        return result

    def calc(self, resonant=False):
        result = []
        for char in self.charset:
            for x1, y1, x2, y2, dx, dy in self.delta_xy(ord(char)):
                line = self.find_line(x1, y1, x2, y2, dx, dy)
                dist = self.euc_dist(np.array((x1, y1)), np.array((x2, y2)))
                antinodes = self.find_antinodes(line, np.array((x1, y1)), np.array((x2, y2)), dist, resonant=resonant)
                if antinodes:
                    result.extend(antinodes)
        return len(set(result))


if __name__ == '__main__':
    sol = Solution()
    print(sol.calc(resonant=False))
    print(sol.calc(resonant=True))
