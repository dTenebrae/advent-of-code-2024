import time
import math
from itertools import chain
from collections import defaultdict


class Solution:

    @staticmethod
    def input_open(file_path):
        try:
            with open(file_path, "r") as f:
                data = list(map(int, f.read().strip().split()))
        except FileNotFoundError:
            print("File not found. Exiting")
            exit(1)

        return data

    def __init__(self, file_path='../input.txt'):
        self.data = self.input_open(file_path)
        self.memo = {
            0: (1,),
            1: (2024,),
        }
        self.cache = defaultdict(int)
        for num in self.data:
            self.cache[num] += 1

    @staticmethod
    def num_split_str(num, num_len) -> tuple:
        str_stone = f"{num}"
        middle = num_len // 2
        return int(str_stone[:middle]), int(str_stone[middle:])

    def process_stones(self, stone: int):
        if self.memo.get(stone):
            return self.memo[stone]

        stone_len = len(str(stone))
        if stone_len % 2 == 0:
            self.memo[stone] = self.num_split_str(stone, stone_len)
            return self.memo[stone]
        else:
            self.memo[stone] = stone * 2024,
            return self.memo[stone]

    def first_calc(self, n=25):

        for _ in range(n):
            tmp_freq = defaultdict(int)
            for num, cnt in self.cache.items():
                for item in self.process_stones(num):
                    tmp_freq[item] += cnt
            self.cache = tmp_freq

        return sum(self.cache.values())

if __name__ == '__main__':
    sol = Solution()
    n = 75
    start = time.time()
    result = sol.first_calc(n)
    end = time.time()
    print(f"iterations: {n:<5} elapsed time: {end - start:3f}s result: {result:^5}")
