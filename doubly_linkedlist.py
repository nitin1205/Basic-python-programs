class Node:
    def __init__(self,value=None):
        self.prev = None
        self.value = value
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def insert(self,value,position):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            if position == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                new_node.prev = None
            else:
                temp_node = self.head
                i = 1
                while i < position:
                    temp_node = temp_node.next
                    i += 1
                if temp_node.next == None:
                    new_node.next = None
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    new_node.next = temp_node.next
                    new_node.prev = temp_node
                    new_node.next.prev =  new_node
                    temp_node.next = new_node

                    
    def display(self):
        if self.head == None:
            print("Linked List is empty.")
        else:
            temp_node = self.head.next
            print(self.head.value)
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
    
    def search(self, key):
        temp_node = self.head
        if self.head == None:
            return f"The linked list is empty."
        elif temp_node.value == key:
            return f"The position of {key} is {0}."
        elif self.tail.value == key:
            return f"The position of {key} is last."
        else:
            i = 0
            while temp_node:
                if temp_node.value == key:
                    return f"The position of {key} is {i}."
                temp_node = temp_node.next
                i += 1
    def reverse_display(self):
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev
    def delete(self,key):
        if self.head == None:
            print("Linked List is empty.")
        else:
            temp_node = self.head
       
            while temp_node:
                if temp_node.value == key and temp_node.prev == None:
                    self.head = self.head.next
                    self.head.prev = None
                    break
                elif temp_node.value == key and temp_node.next == None:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    break
                elif temp_node.value == key:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev
                    break
                temp_node = temp_node.next

doubly_linked_list1 = DoublyLinkedList()
doubly_linked_list1.insert(5,0)
doubly_linked_list1.insert(10,1)
doubly_linked_list1.insert(15,2)
doubly_linked_list1.insert(20,3)

print([node.value for node in doubly_linked_list1])
doubly_linked_list1.display()

doubly_linked_list1.insert(12,2)
print([node.value for node in doubly_linked_list1])
doubly_linked_list1.display()

doubly_linked_list1.insert(1,0)
doubly_linked_list1.insert(25,6)
print([node.value for node in doubly_linked_list1])
doubly_linked_list1.insert(23,6)
print([node.value for node in doubly_linked_list1])
print(doubly_linked_list1.search(23))
doubly_linked_list1.reverse_display()
doubly_linked_list1.delete(1)
print([node.value for node in doubly_linked_list1])
doubly_linked_list1.delete(25)
print([node.value for node in doubly_linked_list1])
doubly_linked_list1.delete(15)
print([node.value for node in doubly_linked_list1])