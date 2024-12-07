import operator
from itertools import product


class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = [(int(k), list(map(int, v.split())))
                        for k, v in map(lambda x: x.split(":"), map(str.strip, f.readlines()))]
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return data

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)

    @staticmethod
    def concat(a, b):
        return int(f"{a}{b}")

    @staticmethod
    def old_validate(line):
        opt = {
            '0': operator.add,
            '1': operator.mul,
        }
        res, vals = line
        bin_len = len(vals) - 1
        max_bin = 2 ** bin_len
        for i in range(max_bin):
            opt_list = list(str(bin(i))[2:].zfill(bin_len))
            cur_cum = vals[0]
            for j in range(1, bin_len + 1):
                cur_cum = opt[opt_list[j - 1]](cur_cum, vals[j])
            if res == cur_cum:
                return res
        return 0

    @staticmethod
    def validate(line, operators):
        res, vals = line
        for ops in product(operators, repeat=len(vals) - 1):
            calc = vals[0]
            for val, op in zip(vals[1:], ops):
                calc = op(calc, val)
            if calc == res:
                return calc
        return 0


    def first_calc(self):
        result = 0
        for line in self.data:
            res = self.validate(line, [operator.add, operator.mul])
            result += res
        return result

    def second_calc(self):
        result = 0
        for line in self.data:
            res = self.validate(line, [operator.add, operator.mul, self.concat])
            result += res
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
