import numpy as np

FILL_VALUE = -1


class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: list(map(lambda y: ord(y), list(x.strip()))), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return np.pad(np.array(data),
                      [(1, 1), (1, 1)],
                      mode='constant',
                      constant_values=FILL_VALUE)

    @staticmethod
    def get_charset(file_path):
        try:
            with open(file_path, "r") as f:
                data = f.read()
                uniq_chars = set(data)
                uniq_chars.remove('\n')
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return uniq_chars

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        self.charset = self.get_charset(file_path)

    def count_square(self, num):
        return len(np.where(self.data == ord(num))[0])

    def count_perim(self, num):
        result = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in zip(*np.where(self.data == ord(num))):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.data[nx, ny] == FILL_VALUE or self.data[nx, ny] != ord(num):
                    result += 1
        return result

    def first_calc(self):
        result = 0
        for char in sol.charset:
            square = self.count_square(char)
            perim = self.count_perim(char)
            result += square * perim
        return result


if __name__ == '__main__':
    sol = Solution('../test.txt')
    print(sol.first_calc())
