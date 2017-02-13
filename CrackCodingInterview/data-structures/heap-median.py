import math


class Heap(object):
    """
    [0, 1, 2, 3, 4]
    """

    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def _get_left_child_value(self, index):
        return self.storage[((index + 1) * 2) - 1]

    def _get_right_child_value(self, index):
        return self.storage[((index + 1) * 2)]

    def _get_parent_value(self, index):
        return self.storage[math.ceil(index/2)-1]
