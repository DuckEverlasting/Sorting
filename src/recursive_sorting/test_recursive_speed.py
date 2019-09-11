import unittest
import random
from recursive_sorting import *

range_with_dupes = []
for _ in range(50):
    range_with_dupes += range(100)

class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr = random.sample(range_with_dupes, 5000)
        self.assertEqual(merge_sort(arr), sorted(arr))
        times = 0.729, 0.647, 0.741
        
        # arr = random.sample(range(10000), 5000)
        # self.assertEqual(merge_sort(arr), sorted(arr))
        # times = 0.793, 0.659, 0.818

        # arr = random.sample(range(100000), 5000)
        # self.assertEqual(merge_sort(arr), sorted(arr))
        # times = 0.675, 0.719, 0.802

if __name__ == '__main__':
    unittest.main()