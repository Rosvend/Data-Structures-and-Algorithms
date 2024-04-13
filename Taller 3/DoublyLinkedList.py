from random import shuffle
from faker import Faker
import time


class Node:
    """The Node class represents a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """The DoublyLinkedList class represents a doubly linked list."""
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the doubly linked list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the doubly linked list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_at_beginning(self):
        """Delete a node from the beginning of the doubly linked list."""
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            temp.next = None
            return temp.data

    def delete_at_end(self):
        """Delete a node from the end of the doubly linked list."""
        if self.is_empty():
            return None
        else:
            current = self.head
            while current.next:
                current = current.next
            if current.prev:
                current.prev.next = None
            else:
                self.head = None
            current.prev = None
            return current.data

    def display(self):
        """Display the doubly linked list."""
        if self.is_empty():
            print("Doubly Linked List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
    
    @staticmethod
    def split_list(head):
        """Split the doubly linked list into two halves."""
        if head is None or head.next is None:
            return None
    
        slow = head # slow is the head of the first half
        fast = head.next # fast is the head of the second half
    
        while fast and fast.next: # find the middle of the doubly linked list
            slow = slow.next # slow moves one node at a time
            fast = fast.next.next # fast moves two nodes at a time
    
        second_half = slow.next # second_half is the head of the second half
        slow.next = None # disconnect the first half from the second half
    
        if second_half: # if the second half is not None
            second_half.prev = None # disconnect the second half from the first half

        return second_half

    
    @staticmethod
    def merge_halves(list1, list2):
        dummy = Node(0)  
        tail = dummy

        
        current1, current2 = list1.head, list2.head

        # Merge process
        while current1 and current2:
            if current1.data < current2.data:
                tail.next, current1.prev = current1, tail
                current1 = current1.next
            else:
                tail.next, current2.prev = current2, tail
                current2 = current2.next
            tail = tail.next

        
        if current1:
            tail.next, current1.prev = current1, tail
        if current2:
            tail.next, current2.prev = current2, tail

        merged_list = DoublyLinkedList(dummy.next)
        if merged_list.head:  
            merged_list.head.prev = None

        return merged_list
    
def merge_sort(dll):
    if dll.head is None or dll.head.next is None:
        return dll

    
    second_half_head = DoublyLinkedList.split_list(dll.head)
    first_half_dll = dll
    second_half_dll = DoublyLinkedList()
    second_half_dll.head = second_half_head

    
    sorted_first_half = merge_sort(first_half_dll)
    sorted_second_half = merge_sort(second_half_dll)

    
    return DoublyLinkedList.merge_halves(sorted_first_half, sorted_second_half)


def measure_time():
    """Function to measure the time of execution of the merge sort algorithm.
    """
    
    N = int(input('Please enter the number of names to sort:  '))
    M = int(input('Please enter the number of times to sort the names: '))
    
    fake = Faker('es_CO') # fake colombian data in spanish, can be changed as needed
    names = [fake.first_name() for _ in range(N)] 
    shuffle(names) #shuffle the names for further randomization


    dll = DoublyLinkedList()
    for name in names:
        dll.insert_at_end(name)

    print("Original list:")
    dll.display()


    tiempo_total = 0
    for i in range(M):
        start_time = time.time()
        sorted_dll = merge_sort(dll)
        end_time = time.time()
        tiempo_total += end_time - start_time
    tiempo_promedio = tiempo_total / M

    print("Sorted list:")
    sorted_dll.display()
    print(f'Tiempo promedio de ejecución: {tiempo_promedio:.10f}')


medirTiempo()