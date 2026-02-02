class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class SLL:
    def __init__(self):
        self.head = None
## creating nodes 
node1 = Node(10) 
node2 = Node(20)
node3 = Node(30)
## linking nodes 
node1.next = node2
node2.next = node3
sll = SLL()
sll.head = node1

print(sll.head)

## traversal in SLL
def traverse_SLL(head):
    current = head
    while current:
        print(current.data,end=" -> ")
        current = current.next
    print(None)
traverse_SLL(sll.head)

## Insertion at head 
def insertion_at_head(head,data):
    new_node = Node(data)
    new_node.next = head
    sll.head = new_node
insertion_at_head(sll.head,5)
traverse_SLL(sll.head)