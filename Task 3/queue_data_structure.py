#To create a Queue data structure

from nodes.node import Node
from LinkedList import LinkedList

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Implement dequeue and display methods
    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":

    print("Queue:")
    queue = LinkedList()
    for data in data_list:
        queue.insert(data)

    print("Original Queue:")
    queue.display()

    print("Dequeue:")
    while queue.head:
        print("Dequeued:", queue.dequeue())


