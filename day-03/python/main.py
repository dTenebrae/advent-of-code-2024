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
        self.re_first = re.compile(r"mul\((\d+),(\d+)\)", re.MULTILINE)
        self.re_second = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

    @staticmethod
    def re_mul(lst: list) -> int:
        lst = list(map(lambda x: tuple(map(int, x)), lst))
        result = sum(map(lambda x: x[0] * x[1], lst))
        return result

    def first_calc(self):
        return sum([self.re_mul(self.re_first.findall(item)) for item in self.data.split('\n')])

    # def second_calc(self):
    #     lst = []
    #     flag = True
    #     for item in self.data:
    #         for idx, slc in enumerate(item.split("don't()")):
    #             if idx == 0 and flag:
    #                 lst.append(slc)
    #                 flag = False
    #                 continue
    #             if "do()" in slc:
    #                 lst.append(slc[slc.index("do()"):])
    #
    #     return sum([self.re_mul(self.re.findall(item)) for item in lst])

    def second_calc(self):
        matches = self.re_second.findall(self.data)

        result = 0
        flag = True
        for match in matches:
            if match == "do()":
                flag = True
            elif match == "don't()":
                flag = False
            elif flag:
                result += self.re_mul(self.re_first.findall(match))
            else:
                continue
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
