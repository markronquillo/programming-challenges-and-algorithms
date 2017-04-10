class MaxHeap(object):
    """
    This assumes that 0 is the start of index counting
    """

    def __init__(self):
        self.storage = []

    def insert(self, value):
        index = len(self.storage)
        self.storage[len(self.storage)] = value
        self._heapify_up(index)

    def remove_max(self, value):
        pass

    def _heapify_up(self, index):
        """
        This means given the index, we compare if it
        is greater than its parent, if yes we swap the values.
        We do this until the parent is greater than the value
        or if it reaches the root
        """
        parent_i = self._get_parent(index)
        if index != 0 and
            self.storage[parent_i] < self.storage[index]:
                self._swap(parent_i, i)
                self._heapify_up(parent_i)

    def _swap(self, index_1, index_2):
        tmp = self.storage[index_1]
        self.storage[index_1] = self.storage[index_2]
        self.storage[index_2] = tmp

    def _heapify_down(self, index):
        """
        Given an index value, we check if its children are greater
        than the current value, if yes we swap the values of the parent
        with the its child that has the highest value
        TODO:
            implement heapify down
            try if I can implement min and max heap tree using one class
        """
        child_lv = self._get_left_child(index)
        child_rv = self._get_right_child(index)
        value = self.storage[index]
        if child_lv > child_rv and child_lv > value:
            child_li = self._get_left_child_index(index)
            self._swap(child_li, index)
            self._heapify_down(child_li)
        elif child_rv >= child_lv and child_rv > value:
            child_ri = self._get_right_child_index(index)
            self._swap(child_ri, index)
            self._heapify_down(child_ri)


    def _get_left_child_index(self, index):
        return ((index + 1) * 2) - 1

    def _get_left_child(self, index):
        return self.storage[self._get_left_child_index(index)]

    def _get_right_child_index(self, index):
        return ((index + 1) * 2)

    def _get_right_child(self, index):
        return self.storage[self._get_right_child_index(index)]

    def _get_parent(self, index):
        return self.storage[math.ceil(index/2)-1]


