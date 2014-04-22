import random
import unittest

from implementations.algorithms.selection import *


class TestSelectionAlgorithms(unittest.TestCase):

    def setUp(self):
        self.elements = random.sample(range(1000), 100)

    def test_quick_select(self):
        data = self.elements[:]
        n = 3
        elm = quick_select(data, k=n)
        self.assertEquals(elm, sorted(self.elements)[n])


if __name__ == '__main__':
    unittest.main()