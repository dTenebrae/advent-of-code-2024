import unittest
from main import Solution

test_list = [
    (3, 4),
    (4, 3),
    (2, 5),
    (1, 3),
    (3, 9),
    (3, 3),
]

class TestMain(unittest.TestCase):

    def setUp(self):
        self.solution = Solution(test_list=test_list)

    def test_first_part(self):
        self.assertEqual(self.solution.get_naive_distance(), 11)

    def test_second_part(self):
        self.assertEqual(self.solution.get_similarity(), 31)

if __name__ == '__main__':
    unittest.main()