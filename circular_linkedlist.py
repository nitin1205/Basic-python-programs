class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def insert(self,value,position):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            if position == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            else:
                temp_node = self.head
                i=1
                while i<position:
                    temp_node = temp_node.next
                    i += 1
                if temp_node.next == self.head:
                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head
                else:
                    next_node = temp_node.next
                    temp_node.next = new_node
                    new_node.next = next_node
                    if temp_node == self.tail:
                        self.tail = new_node
                    
    def display(self):
        if self.head == None:
            print("Linked List is empty.")
        else:
            temp_node = self.head.next
            print(self.head.value)
            while temp_node != self.head:
                print(temp_node.value)
                temp_node = temp_node.next

    def delete(self,key):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            if temp_node.value == key:
                   self.head = temp_node.next
                   self.tail.next = temp_node.next
            else:
                node2 = temp_node
                temp_node = temp_node.next
                while temp_node != self.head:
                    if temp_node.value == key and temp_node.next == self.head:
                        self.tail == node2
                        node2.next = self.head
                        break
                    elif temp_node.value == key:
                        node2.next = temp_node.next
                        break
                    node2 = node2.next
                    temp_node = temp_node.next
    
    def search(self,key):
        if self.head == None:
            return "Linked list does not exist."
        else:
            temp_node = self.head
            if temp_node.value == key:
                return f"The position of {key} is {0}."
            else:
                temp_node = temp_node.next
                i = 1
                while temp_node != self.head:
                    if temp_node.value == key:
                        return f"the position of {key} is {i}."
                    temp_node = temp_node.next
                    i += 1
                return "The key does not exist." 

                

circular_linked_list1 = CircularLinkedList()
circular_linked_list1.insert(5,0)
circular_linked_list1.insert(10,1)
circular_linked_list1.insert(15,2)
circular_linked_list1.insert(20,3)
circular_linked_list1.display()
print([node.value for node in circular_linked_list1])

circular_linked_list1.insert(0,0)
circular_linked_list1.insert(18,2)
circular_linked_list1.insert(25,4)

circular_linked_list1.display()

print([node.value for node in circular_linked_list1])
circular_linked_list1.insert(30,7)
circular_linked_list1.display()

print([node.value for node in circular_linked_list1])

circular_linked_list1.delete(0)
print([node.value for node in circular_linked_list1])
circular_linked_list1.delete(30)
print([node.value for node in circular_linked_list1])
circular_linked_list1.delete(25)
print([node.value for node in circular_linked_list1])
print(circular_linked_list1.tail.next.value)

print(circular_linked_list1.search(5))
print(circular_linked_list1.search(25))
print(circular_linked_list1.search(20))
print(circular_linked_list1.search(30))