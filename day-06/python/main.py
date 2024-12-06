import numpy as np
from itertools import cycle


class Solution:

    def input_open(self, file_path):

        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: list(map(lambda y: self.conv_map[y], list(x.strip()))), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return np.pad(np.array(data),
                      [(1, 1), (1, 1)],
                      mode='constant',
                      constant_values=-1)

    def __init__(self, file_path='../input.txt'):
        self.conv_map = {
            '.': 0,
            '#': 8,
            '^': 1,
        }
        self.path_inc = (
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        )
        self.data = self.input_open(file_path)

    def get_idx(self, cell):
        idx = np.where(self.data == self.conv_map[cell])
        return int(idx[0][0]), int(idx[1][0])

    def walk(self):
        result = set()
        x, y = self.get_idx(cell="^")
        for row_inc, col_inc in cycle(self.path_inc):
            while True:
                current_cell = self.data[x, y]
                if current_cell == -1:
                    return result
                elif current_cell == self.conv_map["#"]:
                    x, y = x - row_inc, y - col_inc
                    break
                else:
                    result.add((x, y))
                    x, y = x + row_inc, y + col_inc

    def first_calc(self):
        return len(self.walk())


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
