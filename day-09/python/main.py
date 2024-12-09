import numpy as np

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

    @staticmethod
    def is_monotonic(seq) -> bool:
        diff = np.diff(seq)
        return all(diff == 1) or all(diff == -1)

    @staticmethod
    def get_free_mem(tr_array: list):
        all_empty = np.where(np.array(tr_array) == EMPTY)[0]
        diff = np.diff(all_empty)
        breaks = np.where(diff != 1)[0] + 1
        return np.split(all_empty, breaks)

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
    def compactify_first(tr_array: list):
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

    def compactify_second(self, tr_array: list):
        free_mem = self.get_free_mem(tr_array)
        arr = np.array(tr_array)
        max_val = max(arr)
        for num in range(max_val, -1, -1):
            where_num = np.where(arr == num)[0]
            needed_len = len(where_num)
            # find free space in memory list
            for i, mem in enumerate(free_mem):
                if len(mem) < needed_len:
                    continue
                if where_num[0] <= mem[0]:
                    break
                for idx in range(needed_len):
                    arr[mem[idx]] = num
                # Clean up copied values
                arr[where_num] = EMPTY
                # Delete used memory from list
                free_mem[i] = np.delete(free_mem[i], range(needed_len))
                break

        return arr

    @staticmethod
    def summarize(cmp_arr: list):
        return sum([num * item for num, item in enumerate(cmp_arr) if item != EMPTY])


if __name__ == '__main__':
    sol = Solution()
    transformed = sol.transform()
    compacted_first = sol.compactify_first(transformed.copy())
    print(sol.summarize(compacted_first))
    compacted_second = sol.compactify_second(transformed)
    print(sol.summarize(compacted_second))
