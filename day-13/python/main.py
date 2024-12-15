import re

SECOND_ADJ = '10000000000000'


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

    @staticmethod
    def cramer_solver(equation: list):
        det = equation[0] * equation[3] - equation[2] * equation[1]
        det_a = equation[4] * equation[3]  - equation[2] * equation[5]
        det_b = equation[0] * equation[5]  - equation[4] * equation[1]

        if det == 0:
            return None

        a, b = det_a / det, det_b / det
        if (a != int(a)) or (b != int(b)):
            return None
        return int(a), int(b)

    def get_tokens(self, item):
        res = self.cramer_solver(item)
        if res is None:
            return 0
        a, b = res
        return 3 * a + 1 * b

    def first_calc(self):
        result = sum([self.get_tokens(item) for item in self.data])
        return result

    def adjust_data(self):
        def update_data(seq):
            for num in range(-1, -3, -1):
                seq[num] = int(SECOND_ADJ + f"{seq[num]}")

        for item in self.data:
            update_data(item)

    def second_calc(self):
        self.adjust_data()
        return max([self.get_tokens(item) for item in self.data])


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
