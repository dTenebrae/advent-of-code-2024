EMPTY = -1


class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = f.read().strip()
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return list(map(int, list(data)))

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)

    def transform(self):
        file_flag = True
        result = []
        file_counter = 0
        for item in self.data:
            if file_flag:
                result.extend([file_counter for _ in range(item)])
                file_counter += 1
            else:
                result.extend([EMPTY for _ in range(item)])
            file_flag = not file_flag
        return result

    @staticmethod
    def compactify(tr_array: list):
        end_ptr = len(tr_array) - 1
        for front_ptr in range(0, len(tr_array)):
            if front_ptr >= end_ptr:
                break
            if tr_array[front_ptr] != EMPTY:
                continue
            for back_ptr in range(end_ptr, -1, -1):
                if tr_array[back_ptr] == EMPTY:
                    continue
                tr_array[front_ptr], tr_array[back_ptr] = tr_array[back_ptr], tr_array[front_ptr]
                end_ptr = back_ptr
                break
        return tr_array

    @staticmethod
    def first_calc(cmp_arr: list):
        return sum([num * item for num, item in enumerate(cmp_arr) if item != EMPTY])


if __name__ == '__main__':
    sol = Solution()
    transformed = sol.transform()
    compacted = sol.compactify(transformed)
    print(sol.first_calc(compacted))
