from random import randint
class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curren_node = self.head
        while curren_node:
            yield curren_node
            curren_node = curren_node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.head == self.tail:
                self.head.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
    
    def generate(self,n , min_value, max_value):
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
    
    def reverse(self):
        while self.tail:
            print(self.tail.value)
            self.tail = self.tail.prev