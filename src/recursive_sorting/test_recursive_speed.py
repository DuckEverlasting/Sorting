import unittest
import random
from recursive_sorting import merge_sort, merge_sort_in_place

range_with_dupes = []
for _ in range(50):
    range_with_dupes += range(100)

class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr = random.sample(range_with_dupes, 5000)
        self.assertEqual(merge_sort(arr), sorted(arr))
        # times = 0.030, 0.029, 0.032
        
        arr = random.sample(range(10000), 5000)
        self.assertEqual(merge_sort(arr), sorted(arr))
        # times = 0.031, 0.032, 0.030

        arr = random.sample(range(100000), 10000)
        self.assertEqual(merge_sort(arr), sorted(arr))
        # times = 0.071, 0.066, 0.066
    
    def test_merge_sort_in_place(self):
        arr = random.sample(range_with_dupes, 5000)
        self.assertEqual(merge_sort_in_place(arr, 0, len(arr) - 1), sorted(arr))
        # times = 0.062, 0.065, 0.061
        
        arr = random.sample(range(10000), 5000)
        self.assertEqual(merge_sort_in_place(arr, 0, len(arr) - 1), sorted(arr))
        # times = 0.083, 0.061, 0.066

        arr = random.sample(range(100000), 10000)
        self.assertEqual(merge_sort_in_place(arr, 0, len(arr) - 1), sorted(arr))
        # times = 0.200, 0.205, 0.227

if __name__ == '__main__':
    unittest.main()