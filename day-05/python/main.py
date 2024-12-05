from collections import defaultdict

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

    def process_data(self):
        first_list, second_list = map(lambda x: x.split('\n'), self.data.split('\n\n'))
        first_list = list(map(lambda x: x.split("|"), first_list))
        second_list = list(map(lambda x: x.split(','), second_list))
        second_list = [item for item in second_list if not (len(item) == 1 and (item[0] == ''))]
        first_dict = defaultdict(list)
        for item in first_list:
            first_dict[item[0]].append(item[1])

        return first_dict, second_list

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        self.rules, self.progs = self.process_data()

    def is_line_valid(self, line: list) -> bool:
        for idx, num in enumerate(line):
            for rule in self.rules[num]:
                if rule in line and line.index(rule) < idx:
                    return False
        return True

    def first_calc(self):
        result = 0
        for line in self.progs:
            if self.is_line_valid(line):
                result += int(line[len(line) // 2])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_calc())
