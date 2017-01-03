
class Node:
    def __init__(self, data):
        self.right=self.left=None
        self.data = data

class Solution:

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else: 
            # this recursion basically is looking for 
            # the right node where to insert the new Node(data)
            # that will be returned in the last recursive call
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def levelOrder(self, root):
        if root:
            queue = [root]
            while queue:
                node = queue.pop()
                if node:
                    print(node.data, '', end='')
                    if node.left:
                        queue.insert(0, node.left)
                    if node.right:
                        queue.insert(0, node.right)


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root ,data)
    (myTree.levelOrder(root))

