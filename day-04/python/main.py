import numpy as np

# Doesn't really matter which number it is, but it should not interfere with conv_map values
FILL_VALUE = -10


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
                # This easy to read construction converting input to list of lists of corresponding digits
                data = list(map(lambda x: list(map(lambda y: conv_map[y], list(x.strip()))), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        # Create some padding for right and bottom. In our scanning algorithm that's enough
        return np.pad(np.array(data),
                      [(0, 3), (0, 3)],
                      mode='constant',
                      constant_values=FILL_VALUE)

    def get_windows(self, window_shape=(4, 4)):
        """
        Create sequence of 2d-windows with stride 1
        """
        return np.lib.stride_tricks.sliding_window_view(self.data, window_shape=window_shape)

    @staticmethod
    def test_seq(seq):
        """
        Test a sequence (1d array) for being monotonic
        """
        diff = np.diff(seq)
        return all(diff == 1) or all(diff == -1)

    def cnt_window_first(self, arr):
        """
        Testing 2 diagonals and 1st row and column for being monotonic and sum that
        """
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
        """
        Counting valid entries
        :param f: validating function
        :param window_shape: rolling window shape. For second question equals to (3, 3)
        :param change_x: Should we change "X" to another number. Needed for second question
        :return:
        """
        result = 0

        if change_x:
            self.data[self.data == 1] = FILL_VALUE

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
