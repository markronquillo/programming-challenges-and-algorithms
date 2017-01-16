class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def insert(self, head, value):
        """ head is a Node type """
        if head is None:
            head = Node(value)
            return head

        if value <= head.data:
            return self.insert(head.left, value)
        else:
            return self.insert(head.right, value



