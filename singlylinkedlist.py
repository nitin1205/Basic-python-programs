#Node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

#linked list class
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node

            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            
            else:
                temp_Node = self.head
                index = 0
                while index < location - 1:
                    temp_Node = temp_Node.next
                    index += 1
                nextNode = temp_Node.next
                temp_Node.next = new_node
                new_node.next = nextNode
                if temp_Node == self.tail:
                    self.tail = new_node

    def display(self):
        if self.head == None:
            print("Linked List is Empty.")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def search(self, key):
        if self.head == None:
            return "linked list is empty"
        else:
            temp_node = self.head
            i = 0
            while temp_node:
                if temp_node.value == key:
                    return f"The position of {key} is {i}"
                temp_node = temp_node.next
                i += 1
            return "The value does not exist."

    def delete(self,key):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            node2 = Node()
            i = 0
            while temp_node:
                if temp_node.value == key and i == 0:
                    self.head = self.head.next
                    break
                elif temp_node.value == key:
                    if temp_node.next == None:
                        self.tail = node2
                        node2.next = None
                        break
                    else:
                        node2.next = temp_node.next
                        break
                node2 = temp_node
                temp_node = temp_node.next
                i += 1 


singlylinkedlist = SLinkedList()
singlylinkedlist.insert(1,0)
singlylinkedlist.insert(2,1)
singlylinkedlist.insert(3,2)
singlylinkedlist.insert(7,3)
singlylinkedlist.insert(15,4)
singlylinkedlist.insert(10,-1)

singlylinkedlist.display()
print([node.value for node in singlylinkedlist])

#singlylinkedlist.insert(13,0)
#singlylinkedlist.insert(13,1)
#singlylinkedlist.display()

#singlylinkedlist2 = SLinkedList()
#singlylinkedlist2.display()

#print(singlylinkedlist.search(7))

singlylinkedlist.delete(1)
singlylinkedlist.delete(10)
singlylinkedlist.delete(7)
print([node.value for node in singlylinkedlist])
print(singlylinkedlist.tail.value)
print(singlylinkedlist.head.value)