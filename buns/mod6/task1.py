class ListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def get_value_at(self, index):
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next_node
            count += 1
        return current.value

    def remove_node(self, index):
        if index < 0:
            return
        if index == 0:
            self.head = self.head.next_node
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next_node
            count += 1
        if current and current.next_node:
            current.next_node = current.next_node.next_node

    def insert_node(self, position, value):
        if position < 0:
            return
        new_node = ListNode(value)
        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next_node
                count += 1
            if current:
                new_node.next_node = current.next_node
                current.next_node = new_node

    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            value = self.current.value
            self.current = self.current.next_node
            return value
