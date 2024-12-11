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

    @staticmethod
    def num_split_str(num, num_len) -> tuple:
        str_stone = f"{num}"
        middle = num_len // 2
        return int(str_stone[:middle]), int(str_stone[middle:])

    @staticmethod
    def num_split_math(num) -> tuple:
        n0 = 1 + int(math.log10(num))
        div = 10 ** (n0 / 2)
        return int(num // div), int(num % div)

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
        stone_list = self.data.copy()
        for _ in range(n):
            tmp_list = []
            for stone in stone_list:
                result = self.process_stones(stone)
                tmp_list.extend(result)
            stone_list = tmp_list
        return stone_list

    def test_calc(self, n=25):
        stone_list = self.data.copy()
        for _ in range(n):
            stone_list = list(chain.from_iterable(map(self.process_stones, stone_list)))
        return stone_list

    @staticmethod
    def simulate_blinks(initial_stones, blinks):
        # Initialize frequency dictionary
        stone_freq = defaultdict(int)
        for stone in initial_stones:
            stone_freq[stone] += 1

        for i in range(1, blinks + 1):
            start_time = time.perf_counter()

            new_stone_freq = defaultdict(int)

            # Process each unique stone and its frequency
            for stone, count in stone_freq.items():
                if stone == '0':
                    new_stone_freq['1'] += count
                elif len(stone) % 2 == 0:
                    half = len(stone) // 2
                    left = str(int(stone[:half]))
                    right = str(int(stone[half:]))
                    new_stone_freq[left] += count
                    new_stone_freq[right] += count
                else:
                    # Multiply by 2024 and convert back to string
                    new_value = str(int(stone) * 2024)
                    new_stone_freq[new_value] += count

            # Update stone frequencies for the next iteration
            stone_freq = new_stone_freq

            # Calculate total stones
            total_stones = sum(stone_freq.values())
            end_time = time.perf_counter()
            time_taken = end_time - start_time
            print(f"Blink {i}: {total_stones} stones > {time_taken:.6f} seconds")


if __name__ == '__main__':
    sol = Solution("../test.txt")
    # n = 25
    # start = time.time()
    # result = len(sol.first_calc(n))
    # end = time.time()
    # print(f"iterations: {n:<2} elapsed time: {end - start:3f}s result: {result}")
    # n = 41
    # start = time.time()
    # result = len(sol.first_calc(n))
    # end = time.time()
    # print(f"iterations: {n:<2} elapsed time: {end - start:3f}s result: {result}")
    sol.simulate_blinks(list(map(str, sol.data)), 41)
    # start = time.time()
    # result = len(sol.test_calc(n))
    # end = time.time()
    # print(f"iterations: {n:<5} elapsed time: {end - start:3f}s result: {result:^5}")
