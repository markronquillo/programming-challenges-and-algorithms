import unittest


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_linked_list(head):
    """
    Given the head, traverses the linked list
    and prints the each of the node values
    """
    if head is None:
        return
    while head is not None:
        print head.value
        head = head.next

def delete_node(node):
    """
    This deletes the given node by copying the value of the next node
    and setting the next value of this node to next node value of its next node :D
    """
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        raise Exception('cannot delete the last node with this method')


