from solution import (
    LinkedListNode,
    delete_node,
    print_linked_list
)

a = LinkedListNode("A")
b = LinkedListNode("B")
c = LinkedListNode("C")

a.next = b
b.next = c
print_linked_list(a)
delete_node(b)
print_linked_list(a)
