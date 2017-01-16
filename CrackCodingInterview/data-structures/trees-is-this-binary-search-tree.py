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
    print lst




