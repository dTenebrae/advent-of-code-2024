from collections import Counter


class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = list(map(lambda x: map(int, x.split()), f.readlines()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return zip(*data)

    def __init__(self, file_path='../input.txt', test_list=None):
        if test_list:
            self.first_list, self.second_list = zip(*test_list)
        else:
            self.first_list, self.second_list = self.input_open(file_path)
        self.counter = Counter(self.second_list)

    def get_naive_distance(self):
        result = 0
        for first, second in zip(sorted(self.first_list), sorted(self.second_list)):
            result += abs(first - second)
        return result

    def get_similarity(self):
        result = 0
        for item in self.first_list:
            if self.counter.get(item):
                result += item * self.counter[item]
        return result

    # proof of concept. It's wrong
    def get_sum_distance(self):
        return abs(sum(self.first_list) - sum(self.second_list))


if __name__ == '__main__':
    sol = Solution()
    print(f"part 1 - {sol.get_naive_distance()}")
    print(f"part 2 - {sol.get_similarity()}")
