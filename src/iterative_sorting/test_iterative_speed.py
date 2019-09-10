import unittest
import random
from iterative_sorting import *

range_with_dupes = []
for _ in range(50):
    range_with_dupes += range(100)

# Uncomment test and parameters you want to run

class IterativeSortingTest(unittest.TestCase):
    def test_null(self):
        pass

    # def test_control(self):
        # arr = random.sample(range_with_dupes, 5000)
        # self.assertEqual(sorted(arr), sorted(arr))
        # times = 0.004, 0.006, 0.004
        
        # arr = random.sample(range(10000), 5000)
        # self.assertEqual(sorted(arr), sorted(arr))
        # times = 0.006, 0.005, 0.005

        # arr = random.sample(range(100000), 5000)
        # self.assertEqual(sorted(arr), sorted(arr))
        # times = 0.007, 0.005, 0.006

    # def test_selection_sort(self):
        # arr = random.sample(range_with_dupes, 5000)
        # self.assertEqual(selection_sort(arr), sorted(arr))
        # times = 0.857, 0.874, 1.026
        
        # arr = random.sample(range(10000), 5000)
        # self.assertEqual(selection_sort(arr), sorted(arr))
        # times = 0.788, 0.761, 0.774

        # arr = random.sample(range(100000), 5000)
        # self.assertEqual(selection_sort(arr), sorted(arr))
        # times = 0.787, 0.931, 0.769

    # def test_bubble_sort(self):
        # arr = random.sample(range_with_dupes, 5000)
        # self.assertEqual(bubble_sort(arr), sorted(arr))
        # times = 11.712, 12.427, 11.220

        # arr = random.sample(range(10000), 5000)
        # self.assertEqual(bubble_sort(arr), sorted(arr))
        # times = 10.835, 10.589, 10.681

        # arr = random.sample(range(100000), 5000)
        # self.assertEqual(bubble_sort(arr), sorted(arr))
        # times = 10.548, 10.994, 10.468

    # def test_counting_sort(self):
        # arr = random.sample(range_with_dupes, 5000)
        # self.assertEqual(count_sort(arr), sorted(arr))
        # times = 0.028, 0.045, 0.029
        
        # arr = random.sample(range(10000), 5000)
        # self.assertEqual(count_sort(arr), sorted(arr))
        # times = 3.037, 2.504, 2.867

        # arr = random.sample(range(100000), 5000)
        # self.assertEqual(count_sort(arr), sorted(arr))
        # times = 24.592, 24.427, 26.825

    # def test_better_insertion_sort(self):
        # arr = random.sample(range_with_dupes, 5000)
        # self.assertEqual(better_insertion_sort(arr), sorted(arr))
        # times = 0.166, 0.185, 0.154
        
        # arr = random.sample(range(10000), 5000)
        # self.assertEqual(better_insertion_sort(arr), sorted(arr))
        # times = 0.250, 0.280, 0.289

        # arr = random.sample(range(100000), 5000)
        # self.assertEqual(better_insertion_sort(arr), sorted(arr))
        # times = 0.298, 0.262, 0.264

if __name__ == '__main__':
    unittest.main()
