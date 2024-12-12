import numpy as np
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
        for reg in region:
            x, y = reg
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.data[nx, ny] == FILL_VALUE or self.data[nx, ny] != ord(num):
                    result += 1
        return result

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
        for char in sol.charset:
            region = self.extract_regions(char)
            for reg in region:
                square = self.count_square(reg)
                perim = self.count_perim(char, reg)
                result += square * perim
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
