class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Element inserted successfully.")

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        print("Element inserted successfully.")

    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        current = self.head
        for i in range(position - 2):
            if current is None:
                print("Invalid position.")
                return
            current = current.next

        if current is None:
            print("Invalid position.")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        print("Element inserted successfully.")

    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
        else:
            self.head = self.head.next
            print("Element deleted successfully.")

    def delete_end(self):
        if self.head is None:
            print("List is empty.")
        elif self.head.next is None:
            self.head = None
            print("Element deleted successfully.")
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            print("Element deleted successfully.")

    def delete_position(self, position):
        if self.head is None:
            print("List is empty.")
            return

        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.delete_beginning()
            return

        current = self.head
        for i in range(position - 2):
            if current.next is None:
                print("Invalid position.")
                return
            current = current.next

        if current.next is None:
            print("Invalid position.")
            return

        current.next = current.next.next
        print("Element deleted successfully.")

    def search(self, data):
        current = self.head
        position = 1

        while current is not None:
            if current.data == data:
                print("Element found at position", position)
                return
            current = current.next
            position += 1

        print("Element not found.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


sll = SinglyLinkedList()

while True:
    print("\n--- SINGLY LINKED LIST ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete at Specific Position")
    print("7. Search")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        sll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        sll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        sll.insert_position(data, position)

    elif choice == 4:
        sll.delete_beginning()

    elif choice == 5:
        sll.delete_end()

    elif choice == 6:
        position = int(input("Enter position: "))
        sll.delete_position(position)

    elif choice == 7:
        data = int(input("Enter element to search: "))
        sll.search(data)

    elif choice == 8:
        sll.display()

    elif choice == 9:
        print("Exit")
        break

    else:
        print("Invalid choice.")