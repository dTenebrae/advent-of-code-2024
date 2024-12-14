import numpy as np
from itertools import groupby
from scipy.ndimage import label

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

    @staticmethod
    def count_square(region):
        return len(region)

    def count_perim(self, num, region):
        result = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in region:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.data[nx, ny] == FILL_VALUE or self.data[nx, ny] != ord(num):
                    result += 1
        return result

    @staticmethod
    def n_monotonics(seq):
        seq = [item[0] for item in seq]
        diff = np.diff(seq)
        breaks = np.where(diff != 1)[0] + 1
        return len(np.split(seq, breaks))

    def real_counter(self, left: list, right: list) -> int:
        result = 0
        # Сортируем по 2-му элементу кортежа с координатами
        # так как мы смотрим только вертикальные стороны(горизонтальных будет столько же)
        left = sorted(left, key=lambda x: x[1])
        right = sorted(right, key=lambda x: x[1])
        # Формируем группы по столбцам
        split_left = [list(g) for k,g in groupby(left, lambda x: x[1])]
        split_right = [list(g) for k,g in groupby(right, lambda x: x[1])]
        # считаем сколько монотонных последовательностей среди таких групп
        for side in [split_left, split_right]:
            for item in side:
                result += self.n_monotonics(item)
        return result * 2

    def count_sides(self, num, region):
        left_side = []
        right_side = []
        directions = [(0, -1), (0, 1)]
        for x, y in region:
            for idx, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if self.data[nx, ny] == FILL_VALUE or self.data[nx, ny] != ord(num):
                    if idx == 0:
                        left_side.append((x, y))
                    else:
                        right_side.append((x, y))
        return self.real_counter(left_side, right_side)

    def extract_regions(self, value):
        binary_matrix = (self.data == ord(value)).astype(int)
        labeled_matrix, num_features = label(binary_matrix)

        regions = []
        for region_id in range(1, num_features + 1):
            coords = np.argwhere(labeled_matrix == region_id)
            regions.append(coords.tolist())

        return regions

    def first_calc(self):
        result = 0
        for char in self.charset:
            regions = self.extract_regions(char)
            for reg in regions:
                square = self.count_square(reg)
                perim = self.count_perim(char, reg)
                result += square * perim
        return result

    def second_calc(self):
        result = 0
        for char in self.charset:
            regions = self.extract_regions(char)
            for reg in regions:
                square = self.count_square(reg)
                sides = self.count_sides(char, reg)
                result += square * sides
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
