class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Stack:

    def __init__(self):
        self.top = None  

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def print(self):
        current = self.top
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


stack = Stack()
stack.push(1)
stack.push(2)
stack.print()  
print(stack.pop())  
stack.print()
