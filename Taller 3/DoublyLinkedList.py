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
    
    def split_list(head):
        """Split the doubly linked list into two halves."""
        if head is None:
            return None, None
    
        slow = head # slow is the head of the first half
        fast = head # fast is the head of the second half
    
        while fast is not None and fast.next is not None: # find the middle of the doubly linked list
            slow = slow.next # slow moves one node at a time
            fast = fast.next.next # fast moves two nodes at a time
    
        second_half = slow.next # second_half is the head of the second half
        slow.next = None # disconnect the first half from the second half
    
        if second_half is not None: # if the second half is not None
            second_half.prev = None # disconnect the second half from the first half

        return head, second_half

    def merge_halves(first_half, second_half):
        """Merge the two halves of the doubly linked list."""
        if first_half is None:
            return second_half
        if second_half is None:
            return first_half
    
        # Encontrar el final de la primera mitad
        current = first_half
        while current.next is not None:
            current = current.next
    
        # Conecta el final de la primera mitad con el inicio de la segunda mitad
        current.next = second_half
        second_half.prev = current
    
        return first_half