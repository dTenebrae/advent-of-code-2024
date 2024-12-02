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
    def is_asc(tup: tuple, thr=0) -> bool:
        result = True
        for idx in range(0, len(tup) - 1):
            if tup[idx] >= tup[idx + 1]:
                result = False
                break
        return result

    @staticmethod
    def is_desc(tup: tuple, thr=0) -> bool:
        result = True
        for idx in range(0, len(tup) - 1):
            if tup[idx] <= tup[idx + 1]:
                result = False
                break
        return result

    @staticmethod
    def is_too_far(tup, thr=0):
        result = True
        for idx in range(0, len(tup) - 1):
            diff = abs(tup[idx] - tup[idx + 1])
            if diff < 1 or diff > 3:
                result = False
                break
        return result

    def tuple_check(self, tup: tuple, thr=0) -> bool:
        return self.is_too_far(tup) and (self.is_asc(tup) or self.is_desc(tup))

    def first_calc(self):
        return sum(map(self.tuple_check, self.data))


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
