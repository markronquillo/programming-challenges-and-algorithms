class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if head is None:
        return False

    current = head   
    nodes = set()
    while current.next is not None:
        if current in nodes:
            return True
        nodes.add(current)

    return False