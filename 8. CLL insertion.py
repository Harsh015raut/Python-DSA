class Node: 
    def __init__(self,data):
        self.data = data 
        self.next = None 

class CLL:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def display(self):
        if self.head is None: 
            print("Cicurlar Linked List is Empty")
        else: 
            temp = self.head 
            print(temp.data,"-->",end = " ")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data,"-->",end = " ")
            print(temp.next.data)  # To print the starting Node again to show CLL 
    
    def add_begin(self,x):
        new = Node(x)
        if self.head is None: 
            self.head = new 
            self.tail = new 
            self.tail.next = self.head 
        else: 
            new.next = self.head 
            self.tail.next = new 
            self.head = new 

    def add_end(self,x):
        new = Node(x) 
        if self.head is None: 
            self.head = new 
            self.tail = None 
            self.tail.next = self.head 
        else:
            self.tail.next = new 
            self.tail = new 
            self.tail.next = self.head 

    def add_pos(self,pos,x):
        new = Node(x)
        if self.head is None:
            self.head = new 
            self.tail = new 
            self.tail.next = self.head  
        else: 
            if pos==1:
                add_begin(x)
            else: 
                temp = self.head 
                for i in range(1,pos-1):
                    temp = temp.next 
                new.next = temp.next 
                temp.next = new 
       

L = CLL()
L.add_begin(10)
L.add_begin(20)
L.add_begin(30)
L.add_end(40)
L.add_pos(3,5)
L.display()