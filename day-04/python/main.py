import numpy as np

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

        return np.pad(np.array(data),
                      [(0, 3), (0, 3)],
                      mode='constant',
                      constant_values=666)

    def get_windows(self):
        return np.lib.stride_tricks.sliding_window_view(self.data, window_shape=(4, 4))

    @staticmethod
    def test_seq(seq):
        diff = np.diff(seq)
        return all(diff == 1) or all(diff == -1)

    def cnt_window(self, arr):
        return sum(
            (
                self.test_seq(arr[:, 0]),
                self.test_seq(arr[0, :]),
                self.test_seq(arr.diagonal())),
                self.test_seq(np.diag(np.fliplr(arr)))
        )

    def first_calc(self):
        result = 0
        windows = self.get_windows()
        for i in range(0, windows.shape[0]):
            for j in range(0, windows.shape[1]):
                tst_window = windows[i][j]
                result += self.cnt_window(tst_window)
        return result

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
