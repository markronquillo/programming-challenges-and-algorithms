class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree(root):
    lst = []
    def traverse(current, l):
        """inorder traversal"""
        if current is not None:
            traverse(current.left, l)
            l.append(current.data)
            traverse(current.right, l)

    traverse(root, lst)

    if len(set(lst)) <> len(lst):
        return False

    if sorted(lst) == lst:
        return True
    else:
        return False


head = node(10)
left = node(5)
right = node(14)

head.left = left
head.right = right

random = node(6)
left.right = random

print(check_binary_search_tree(head))


