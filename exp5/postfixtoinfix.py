class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print("Item inserted successfully")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print("Deleted item:", item)

    def peek(self):
        if self.front == -1:
            print("Queue Underflow")
        else:
            print("Front item is", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue Underflow")
        else:
            i = self.front
            print("Queue elements:")
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()


n = int(input("Enter capacity: "))
q = CircularQueue(n)

while True:
    print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = int(input("Enter item: "))
        q.enqueue(item)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    elif ch == 5:
        print("Exit")
        break