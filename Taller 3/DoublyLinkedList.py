class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
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
        if self.is_empty():
            print("Doubly Linked List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
    
    def split_list(head):
        if head is None:
            return None, None
    
        slow = head
        fast = head
    
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
    
        second_half = slow.next
        slow.next = None
    
        if second_half is not None:
            second_half.prev = None
    
        return head, second_half

    def merge_halves(first_half, second_half):
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