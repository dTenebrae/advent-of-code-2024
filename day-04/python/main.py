import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

class Solution:

    @staticmethod
    def input_open(file_path):
        conv_map = {
            'X': 1,
            'M': 2,
            'A': 3,
            'S': 4,
        }
        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: list(map(lambda y: conv_map[y], list(x.strip()))), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return np.array(data)

    def get_windows(self):
        return np.lib.stride_tricks.sliding_window_view(self.data, window_shape=(4, 4))

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        # print(self.get_windows())


if __name__ == '__main__':
    sol = Solution()
