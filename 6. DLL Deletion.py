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
                print(temp.data,"-->",end=' ')
                temp = temp.next 
    
    def delete_beginning(self):
        temp = self.head 
        self.head = temp.next 
        temp.next = None 
        self.head.prev = None 

    def delete_end(self):
        temp = self.head.next 
        before = self.head 
        while temp.next is not None:
            temp = temp.next 
            before = before.next 
        before.next = None 
        temp.prev = None 
    
    def delete_position(self,pos):
        temp = self.head.next 
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next 
            before = before.next 
        before.next = temp.next 
        temp.next.prev = before 
        temp.next = None 
        temp.prev = None 



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

# L.delete_beginning()
# L.delete_end()
L.delete_position(3)
L.display()