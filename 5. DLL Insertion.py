class Node: 
    def __init__(self,data):
        self.data = data 
        self.prev = None 
        self.next = None 
class DLL:
    def __init__(self):
        self.head = None 
    
    def display(self):
        if self.head is None:
            print("Empty Double Linked List")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next 
            
    def insert_beginning(self,data):
        n = Node(data)
        temp = self.head
        temp.prev = n 
        n.next = temp 
        self.head = n 

    def insert_end(self,data):
        n = Node(data)
        temp = self.head 
        while temp.next:
            temp = temp.next 
        temp.next = n 
        n.prev = temp 

    def insert_position(self,pos,data):
        n = Node(data)
        temp = self.head 
        for i in range(1,pos-1):
            temp = temp.next 
        n.prev = temp
        n.next = temp.next 
        temp.next.prev = n 
        temp.next = n

    


L = DLL()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n2.prev = n1 
n1.next = n2 
n3 = Node(30)
n3.prev = n2 
n2.next = n3 
n4 = Node(40)
n3.next = n4
n4.prev = n3

L.insert_beginning(5)
L.insert_end(60)
L.insert_position(3,15)
L.display()