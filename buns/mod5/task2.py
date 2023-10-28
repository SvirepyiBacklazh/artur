class Node:
    def __init__(self, data):
        self.data = data  
        self.nref = None  
        self.pref = None 

class Queue:

    def __init__(self):
        self.start = None  
        self.end = None  

    def is_empty(self):
        return self.start is None

    def pop(self):
        if self.is_empty():
            return None
        data = self.start.data
        if self.start.nref:
            self.start = self.start.nref
            self.start.pref = None
        else:
            self.start = None
            self.end = None
        return data

    def push(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.start = new_node
            self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        if n < 0:
            return
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            for _ in range(n - 1):
                if current is None:
                    return
                current = current.nref
            if current is None:
                return
            new_node.nref = current.nref
            new_node.pref = current
            if current.nref:
                current.nref.pref = new_node
            current.nref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=' ')
            current = current.nref
        print()


queue = Queue()
queue.push(1)
queue.push(2)
queue.print()  
queue.insert(1, 4)
queue.print()  
print(queue.pop()) 
queue.print()  
