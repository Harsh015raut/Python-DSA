class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None  
    
class SingleLinkedList:
    def __init__(self):
        self.head = None 
    
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head 
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next 

    def delete_begining(self):
        if self.head is None:
            print("Linked list is not present")
        else:
            temp = self.head 
            self.head = temp.next 
            temp.next = None 

    def delete_end(self): 
        prev = self.head 
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next 
            prev = prev.next 
        prev.next = None 

    def delete_position(self,pos):
        prev = self.head 
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next 
            prev = prev.next 
        prev.next = temp.next
        

n = Node(10)
S = SingleLinkedList()
S.head = n 
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(50)
n.next = n1 
n1.next = n2 
n2.next = n3 
n3.next = n4
# S.display()
# S.delete_begining()
# S.delete_end()
S.delete_position(3)
S.display()

