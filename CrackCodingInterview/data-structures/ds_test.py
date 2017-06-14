import unittest

from .ds import MaxHeap


class MaxHeapTest(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()
