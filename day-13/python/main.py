import re

SECOND_ADJ = 10000000000000


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

    def cramer_solver(self, equation: list):
        det = equation[0] * equation[3] - equation[2] * equation[1]
        det_a = equation[4] * equation[3]  - equation[2] * equation[5]
        det_b = equation[0] * equation[5]  - equation[4] * equation[1]

        if det == 0:
            return None

        a, b = det_a / det, det_b / det

        if not self.are_the_same(a) or not self.are_the_same(b) or a < 0 or b < 0:
                return None

        return round(a), round(b)

    def solver(self, equation: list):
        # B = (p_y - p_x * a_y / a_x) / (b_y - a_y * b_x / x_a)
        # A = p_x / a_x - B * b_x / a_x

        b = (equation[5] - equation[4] * equation[1] / equation[0]) / (equation[3] - equation[1] * equation[2] / equation[0])
        a = equation[4] / equation[0] - b * equation[2] / equation[0]

        if not self.are_the_same(a) or not self.are_the_same(b) or a < 0 or b < 0:
            return None

        return int(a), int(b)

    @staticmethod
    def are_the_same(x, epsilon=1e-9) -> bool:
        delta = abs(round(x) - x)
        return delta <= epsilon

    @staticmethod
    def get_tokens(item, f):
        res = f(item)
        if res is None:
            return 0
        a, b = res
        return 3 * a + 1 * b


    def first_calc(self):
        result = sum([self.get_tokens(item, self.cramer_solver) for item in self.data])
        return result

    def adjust_data(self):
        def update_data(seq):
            for num in range(-1, -3, -1):
                seq[num] = SECOND_ADJ + seq[num]

        for item in self.data:
            update_data(item)

    def second_calc(self):
        self.solver(self.data[0])
        self.adjust_data()
        result = [self.get_tokens(item, self.cramer_solver) for item in self.data]
        result = [item for item in result if item]
        return max(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
