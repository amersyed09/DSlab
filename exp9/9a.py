class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new
        print("Item pushed successfully")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Popped item is", self.top.data)
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Top item is", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp = self.top
            print("Stack elements:")
            while temp:
                print(temp.data)
                temp = temp.next


s = Stack()

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        x = int(input("Enter item to push: "))
        s.push(x)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        s.display()
    elif ch == 5:
        print("Exit")
        break