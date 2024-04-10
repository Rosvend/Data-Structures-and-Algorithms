class Node:
    """The Node class represents a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """The DoublyLinkedList class represents a doubly linked list."""
    def __init__(self):
        self.head = None

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
    
    def split_list(self,head):
        """Split the doubly linked list into two halves."""
        if head is None or head.next is None:
            return head
    
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

    def merge_halves(self,first_half, second_half):
        """Merge the two halves of the doubly linked list."""
        if first_half is None:
            return second_half
        if second_half is None:
            return first_half
    
        # Encontrar el final de la primera mitad
        if first_half.data < second_half.data:
            first_half.next = self.merge_halves(first_half.next, second_half)
            first_half.next.prev = first_half
            first_half.prev = None
            return first_half
        else:
            second_half.next = self.merge_halves(first_half, second_half.next)
            second_half.next.prev = second_half
            second_half.prev = None
            return second_half
    
    def merge_sort(self, head):
        """Sort the doubly linked list using the merge sort algorithm."""
        if head is None or head.next is None:
            return head

        second_half = self.split_list(head)
        first_half_sorted = self.merge_sort(head)
        second_half_sorted = self.merge_sort(second_half)

        return self.merge_halves(first_half_sorted, second_half_sorted)
