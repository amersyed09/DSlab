class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        print("Item inserted successfully")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            print("Deleted item is", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            print("Front item is", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            temp = self.front
            print("Queue elements:")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


q = Queue()

while True:
    print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        x = int(input("Enter item to insert: "))
        q.enqueue(x)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    elif ch == 5:
        print("Exit")
        break