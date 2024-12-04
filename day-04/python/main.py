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
                      constant_values=-1)

    def get_windows(self, window_shape=(4, 4)):
        return np.lib.stride_tricks.sliding_window_view(self.data, window_shape=window_shape)

    @staticmethod
    def test_seq(seq):
        diff = np.diff(seq)
        return all(diff == 1) or all(diff == -1)

    def cnt_window_first(self, arr):
        return sum(
            (
                self.test_seq(arr[:, 0]),
                self.test_seq(arr[0, :]),
                self.test_seq(arr.diagonal())),
                self.test_seq(np.diag(np.fliplr(arr)))
        )

    def cnt_window_second(self, arr):
        return self.test_seq(arr.diagonal()) and self.test_seq(np.diag(np.fliplr(arr)))

    def final_count(self, f, window_shape=(4, 4), change_x=False):
        result = 0
        if change_x:
            self.data[self.data == 1] = -10

        windows = self.get_windows(window_shape=window_shape)
        for i in range(0, windows.shape[0]):
            for j in range(0, windows.shape[1]):
                tst_window = windows[i][j]
                result += f(tst_window)
        return result

    def first_calc(self):
        return self.final_count(f=self.cnt_window_first)

    def second_calc(self):
        return self.final_count(f=self.cnt_window_second, window_shape=(3, 3), change_x=True)

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
