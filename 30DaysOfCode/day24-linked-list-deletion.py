class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            tmp = head
            while (tmp.next is not None):
                tmp = tmp.next
            tmp.next = p
        return head


    def display(self, head):
        current = head
        while (current is not None):
            print(current.data, '', end='')
            current = current.next

    def removeDuplicates(self, head):
        if head:
            s = set([head.data])
            current = head
            while (current.next is not None):
                if current.next.data in s:
                    current.next = current.next.next
                    continue
                else:
                    s.add(current.next.data)
                current = current.next
        return head

    # def removeDuplicates(self, head):
    #     s = set()
    #     current = head
    #     prev = None
    #     while (current is not None):
    #         if current.data in s:
    #             prev.next = current.next
    #             current = current.next
    #             continue
    #         else:
    #             s.add(current.data)
    #         prev = current
    #         current = current.next
    #     return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)


