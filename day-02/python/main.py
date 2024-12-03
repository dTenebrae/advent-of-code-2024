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
    def check(tup):
        dist = [tup[i] - tup[i + 1] for i in range(len(tup) - 1)]
        monotonic = all(x > 0 for x in dist) or all(x < 0 for x in dist)
        return all([1 <= abs(item) <= 3 for item in dist]) and monotonic

    def first_calc(self):
        return sum(map(self.check, self.data))

    def second_calc(self):
        return sum(map(lambda x: sum([self.check(x[:i] + x[i + 1:]) for i in range(len(x))]) > 0, self.data))


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
    print(sol.second_calc())
