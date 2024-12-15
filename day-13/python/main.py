import re


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

    def first_calc(self):
        result = 0
        for item in self.data:
            res = self.cramer_solver(item)
            if res is None:
                continue
            a, b = res
            result += 3 * a + b
        return result



if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
