def enqueue():
    n = int(input("Enter the element to be inserted into queue"))
    queue.append(n)

def dequeue():
    if len(queue) == 0:
        print("QUEUE IS EMPTY")
    else:
        print(queue[0]," is the element deleted from queue")
        del queue[0]
        print()

def display():
    if len(queue)==0:
        print("QUEUE IS EMPTY")
    else:
        print("ELEMENTS OF QUEUE ARE")
        for ele in queue:
            print(ele,end=" ")
        print("Front of the queue is ",queue[0])
        print("End of the queue is ",queue[-1])

queue = list()
while(1):
    print("Enter the option from below: \n1.Enqueue Operation\n2.Dequeue Operation\n3.Display\n4.Exit")
    option = int(input())
    if option == 1:
        print("ENQUEUE OPERATION")
        enqueue()
    elif option == 2:
        print("DEQUEUE OPERATION")
        dequeue()
    elif option == 3:
        print("DISPLAY")
        display()
    else:
        break