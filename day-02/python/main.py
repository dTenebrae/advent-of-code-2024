class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: tuple(map(int, x.split())), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return data

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)

    @staticmethod
    def is_asc(tup: tuple) -> bool:
        result = True
        for idx in range(0, len(tup) - 1):
            if tup[idx] >= tup[idx + 1]:
                result = False
                break
        return result

    @staticmethod
    def is_desc(tup: tuple) -> bool:
        result = True
        for idx in range(0, len(tup) - 1):
            if tup[idx] <= tup[idx + 1]:
                result = False
                break
        return result

    @staticmethod
    def is_not_too_far(tup):
        result = True
        for idx in range(0, len(tup) - 1):
            diff = abs(tup[idx] - tup[idx + 1])
            if diff < 1 or diff > 3:
                result = False
                break
        return result

    @staticmethod
    def func_iter(tup, f):
        for idx in range(len(tup)):
            test_lst = list(tup)
            test_lst.pop(idx)
            if f(test_lst):
                return test_lst, True
        return tup, False

    def tuple_check(self, tup: tuple) -> bool:
        return self.is_not_too_far(tup) and (self.is_asc(tup) or self.is_desc(tup))

    def tuple_check2(self, tup: tuple) -> bool:
        counter = 0
        not_far = self.is_not_too_far(tup)
        if not not_far:
            counter = 1
            tup, not_far = self.func_iter(tup, self.is_not_too_far)

        if not not_far:
            return False

        result = self.is_desc(tup) or self.is_asc(tup)
        if result:
            return True

        if counter:
            return False
        else:
            result = self.func_iter(tup, self.is_desc)[1] or self.func_iter(tup, self.is_asc)[1]
            return result

    @staticmethod
    def check(tup):
        dist = [tup[i] - tup[i + 1] for i in range(len(tup) - 1)]
        monotonic = all(x > 0 for x in dist) or all(x < 0 for x in dist)
        return all([1 <= abs(item) <= 3 for item in dist]) and monotonic


    def first_calc(self):
        return sum(map(self.check, self.data))

    def second_calc(self):
        return sum(map(lambda x: sum([self.check(x[:i] + x[i + 1:]) for i in range(len(x))]) > 0, self.data))

    def print_out(self):
        for item in self.data:
            print(f"{item} -> {self.tuple_check2(item)}")


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
    # sol.print_out()
