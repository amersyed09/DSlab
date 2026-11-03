class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            current.next = new_node
            self.head = new_node

        print("Element inserted successfully.")

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

        print("Element inserted successfully.")

    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        if self.head is None:
            print("Invalid position.")
            return

        current = self.head

        for i in range(position - 2):
            current = current.next

            if current == self.head:
                print("Invalid position.")
                return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

        print("Element inserted successfully.")

    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            self.head = self.head.next
            current.next = self.head

        print("Element deleted successfully.")

    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head

            while current.next.next != self.head:
                current = current.next

            current.next = self.head

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
            current = current.next

            if current.next == self.head:
                print("Invalid position.")
                return

        if current.next == self.head:
            print("Invalid position.")
            return

        current.next = current.next.next
        print("Element deleted successfully.")

    def search(self, data):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        position = 1

        while True:
            if current.data == data:
                print("Element found at position", position)
                return

            current = current.next
            position += 1

            if current == self.head:
                break

        print("Element not found.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")


cll = CircularLinkedList()

while True:
    print("\n--- CIRCULAR LINKED LIST ---")
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
        cll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        cll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        cll.insert_position(data, position)

    elif choice == 4:
        cll.delete_beginning()

    elif choice == 5:
        cll.delete_end()

    elif choice == 6:
        position = int(input("Enter position: "))
        cll.delete_position(position)

    elif choice == 7:
        data = int(input("Enter element to search: "))
        cll.search(data)

    elif choice == 8:
        cll.display()

    elif choice == 9:
        print("Exit")
        break

    else:
        print("Invalid choice.")