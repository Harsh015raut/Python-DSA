class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None 
    def push(self):
        x = int(input("Enter element to be inserted into stack"))
        new = Node(x)
        if self.top is None:
            self.top = new 
            self.top.next = None 
        else:
            new.next = self.top 
            self.top = new 
    def pop(self):
        if self.top is None:
            print("STACK IS EMPTY")
        elif self.top.next is None:
            print("Popped Element is :", self.top.data) 
            print("-----------------------------------")
            self.top = None
        else:
            temp = self.top 
            print("Popped Element is :", self.top.data) 
            print("-----------------------------------")
            self.top = temp.next 
            temp = None
    
    def display(self):
        if self.top is None:
            print("STACK IS EMPTY")
            print("-----------------------------------")
        else:
            print("ELEMENTS OF STACK ARE:")
            temp = self.top 
            while temp:
                print(temp.data)
                temp = temp.next
            print("TOP OF THE STACK IS ",self.top.data)
            print("-----------------------------------")


     

s = Stack()
while(1):
    print("ENter the Option from Below")
    print("1. Push Operation\n2. Pop Operation\n3. Display\n4. Exit")
    option = int(input())
    if option == 1:
        print("PUSH OPERATION")
        print("--------------")
        s.push()
    elif option == 2:
        print("POP OPERATION")
        print("--------------")
        s.pop()
    elif option == 3:
        print("Display")
        print("--------------")
        s.display()
    else:
        break