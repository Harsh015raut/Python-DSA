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
            print("Circular Linked List is empty")
        else:
            temp = self.head 
            print(temp.data,"-->",end=" ")
            while temp.next != self.head:
                temp = temp.next 
                print(temp.data,"-->",end = " ")
            print(temp.next.data)
    
    def search(self):
        x = int(input("Enter element to be searched in CLL: "))
        temp = self.head 
        count = 0 
        flag = 0 
        while(temp != self.tail):
            if x==temp.data:
                flag = 1 
                break 
            temp = temp.next 
            count = count + 1 
        else:
            if x==temp.data:
                flag = 1
        if flag == 1:
            print(x,"is found at position - ",count+1)
        else:
            print(x," is not found in Circular Linked List")
            
L = CLL()
n1 = Node(10) 
L.head = n1 
L.tail = n1 
L.tail.next = L.head 
L.display()

n2 = Node(20) 
L.tail.next = n2 
L.tail = n2 
L.tail.next = L.head 
L.display()

n3 = Node(30) 
L.tail.next = n3 
L.tail = n3 
L.tail.next = L.head 
L.display()

n4 = Node(40) 
L.tail.next = n4 
L.tail = n4 
L.tail.next = L.head 
L.display()

L.search()