# node class
class Node:
    def __init__(self, value=None):
        self.left = None
        self.value = value
        self.right = None
        
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                        break
                    current_node = current_node.left
                        
                else:
                    if current_node.right == None:
                        current_node.right = new_node
                        break
                    current_node = current_node.right
                    
    def search(self, value):
        current_node = self.root
        if current_node.value == None:
            return False
        else:
            while True:
                if value < current_node.value:
                    current_node = current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
                else:
                    return current_node
             
            
    def node(self):
        print(self.root.value)
            
            
    def traverse(self):
        current_node = self.root
        
            
            
            
            
bintree = BinarySearchTree()
bintree.insert(15)
bintree.insert(29)
bintree.insert(19)
bintree.insert(27)
bintree.insert(47)
bintree.node()

x = bintree.search(19)
print(x)
print(x.value)
print(x.left)
print(x.right.value)