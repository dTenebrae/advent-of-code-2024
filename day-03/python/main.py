import re

class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = f.read()
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return data

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        self.re = re.compile(r"mul\((\d+),(\d+)\)", re.MULTILINE)
        self.test_str = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    @staticmethod
    def re_mul(lst: list) -> int:
        lst = list(map(lambda x: tuple(map(int, x)), lst))
        result = sum(map(lambda x: x[0] * x[1], lst))
        return result

    def first_calc(self):
        return self.re_mul(self.re.findall(self.data))


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
