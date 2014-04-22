import random
import unittest

from implementations.algorithms.sort import *


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.elements = random.sample(range(1000), 100)

    def test_shellsort(self):
        data = self.elements[:]
        shellsort(data)
        self.assertEquals(data, sorted(self.elements))

    def test_quicksort(self):
        data = self.elements[:]
        quicksort(data)
        self.assertEquals(data, sorted(self.elements))

    def test_bubblesort(self):
        data = self.elements[:]
        bubblesort(data)
        self.assertEquals(data, sorted(self.elements))

    def test_shakersort(self):
        data = self.elements[:]
        shakersort(data)
        self.assertEquals(data, sorted(self.elements))

    def test_selectionsort(self):
        data = self.elements[:]
        selectionsort(data)
        self.assertEquals(data, sorted(self.elements))

    def test_insertionsort(self):
        data = self.elements[:]
        insertionsort(data)
        self.assertEquals(data, sorted(self.elements))

    def test_mergesort(self):
        data = mergesort(self.elements)
        self.assertEquals(data, sorted(self.elements))

if __name__ == '__main__':
    unittest.main()