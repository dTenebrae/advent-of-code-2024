import re

SECOND_OFFSET = 10000000000000


class Solution:

    @staticmethod
    def input_open(file_path):
        regex = re.compile(r"Button A: X\+(\d+),\sY\+(\d+)\sButton\sB:\sX\+(\d+),\sY\+(\d+)\sPrize:\sX=(\d+),\sY=(\d+)")
        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: x.replace("\n", " "), f.read().split('\n\n')))
                data = [list(map(int, regex.findall(item)[0])) for item in data]
                print()
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return data

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)

    def cramer_solver(self, equation: list, offset=0):
        a_x, a_y, b_x, b_y, p_x, p_y = equation
        p_x += offset
        p_y += offset

        det = a_x * b_y - b_x * a_y
        det_a = p_x * b_y - b_x * p_y
        det_b = a_x * p_y - p_x * a_y

        if det == 0:
            return None

        a, b = det_a / det, det_b / det

        if not self.is_valid(a) or not self.is_valid(b):
                return None

        return int(a), int(b)

    @staticmethod
    def is_valid(num: float):
        return num.is_integer() and num >= 0

    @staticmethod
    def get_tokens(item, f, offset):
        res = f(item, offset)
        if res is None:
            return 0
        a, b = res
        return 3 * a + 1 * b

    def calc(self):
        for offset in (0, SECOND_OFFSET):
            result = sum([self.get_tokens(item, self.cramer_solver, offset) for item in self.data])
            print(result)


if __name__ == '__main__':
    sol = Solution()
    sol.calc()
