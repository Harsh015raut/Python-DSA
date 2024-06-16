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
            print("Empty Circular Linked List")
        else: 
            temp = self.head 
            print(temp.data,"-->",end=" ")
            while temp.next != self.head:
                temp = temp.next 
                print(temp.data,"-->",end=" ")
            print(temp.next.data)

L = CLL() 
n1 = Node(10) 
L.head = n1 
L.tail = n1 
L.tail.next = L.head 
print("After first node")
L.display()

n2 = Node(20) 
L.tail.next = n2 
L.tail = n2 
L.tail.next = L.head 
print("After second node")
L.display()

n3 = Node(30) 
L.tail.next = n3 
L.tail = n3 
L.tail.next = L.head 
print("After Third node")
L.display()


         








