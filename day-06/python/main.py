import numpy as np
from copy import deepcopy
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
            '#': 7,
            '^': 1,
        }
        self.path_inc = (
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        )
        self.cycle_thr = 500
        self.data = self.input_open(file_path)

    def get_idx(self, cell):
        idx = np.where(self.data == self.conv_map[cell])
        return int(idx[0][0]), int(idx[1][0])

    def walk(self, arr):
        result = set()
        cycle_cnt = 0
        path_cnt = []

        x, y = self.get_idx(cell="^")
        for row_inc, col_inc in cycle(self.path_inc):
            while True:
                cur_len = len(result)
                path_cnt.append(cur_len)
                if len(path_cnt) > 1 and cur_len == path_cnt[-2]:
                    cycle_cnt += 1
                else:
                    cycle_cnt = 0

                if cycle_cnt > self.cycle_thr:
                    return -1

                current_cell = arr[x, y]
                if current_cell == -1:
                    return len(result)
                elif current_cell == self.conv_map["#"]:
                    x, y = x - row_inc, y - col_inc
                    break
                else:
                    result.add((x, y))
                    x, y = x + row_inc, y + col_inc

    def first_calc(self):
        return self.walk(self.data)

    def second_calc(self):
        result = 0
        idx_lst = [(int(x), int(y)) for x, y in zip(*np.where(self.data == 0))]
        for x, y in idx_lst:
            arr = deepcopy(self.data)
            arr[x, y] = self.conv_map["#"]
            is_cycle = self.walk(arr) == -1
            result += is_cycle
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
