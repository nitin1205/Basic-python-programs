from LinkedList import *

def kth_to_the_last(linkedlist, k):
    temp_node = linkedlist.head
    new_node = Node()
    i = 0
    while i < k:
        temp_node = temp_node.next
        i += 1
    new_node = linkedlist.head
    while temp_node:
        temp_node = temp_node.next
        new_node = new_node.next
    return new_node

def mergeLists(head1, head2):
    node1 = Node(None)
    node2 = Node(None)
    if head1.value < head2.value:
        node1 = head1
        node2 = head1
        head1 = head1.next
        node1.next = None
    elif head2.value < head1.value:
        node1 = head2
        node2 = head2
        head2 = head2.next
        node1.next = None
        
    while head1 and head2:
        if head1.value < head2.value:
            node1.next = head1
            node1 = head1
            head1 = head1.next
            node1.next = None
        elif head2.value < head1.value:
            node1.next = head2
            node1 = head2
            head2 = head2.next
            node1.next = None
        elif head1.value == head2.value:
            node1.next = head1
            node1 = head1
            head1 = head1.next
            
            node1.next = head2
            node1 = head2
            head2 = head2.next
            
    if head1 != None:
        node1.next = head1
        node1 = node1.next
        return node2
    elif head2:
        node1.next = head2
        node1 = node1.next
        return node2

linkedlist1 = LinkedList()
linkedlist2 = LinkedList()
for i in range(10, 17):
    linkedlist1.add(i)
print(linkedlist1)
for j in range(17,20):
    linkedlist2.add(j)
print(linkedlist2)
head = mergeLists(linkedlist1.head,linkedlist2.head)
while head:
    print(head.value)
    head = head.next