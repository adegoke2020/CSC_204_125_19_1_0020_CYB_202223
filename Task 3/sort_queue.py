#using bubble sort to sort the queue
from LinkedList import LinkedList


def sort_queue(self):
    # Convert the linked list to a list for sorting
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next

        # Bubble sort the elements
        n = len(elements)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if elements[j] > elements[j + 1]:
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]

        # Clear the existing linked list and re-insert sorted elements
        self.head = None
        self.tail = None
        for element in elements:
            self.insert(element)

if __name__ == "__main__":

    print("Sorted Queue:")
    queue.sort_queue()
    queue.display()

