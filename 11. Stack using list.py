def push():
    n = int(input("Enter the element to be inserted into stack"))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n," is inserted into Stack")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack[0]," is deleted from stack")
        del stack[0]

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Elements of Stack are")
        for ele in stack:
            print(ele)
        print("Top of the stack is ",stack[0])

stack = list()
while(1):
    print("Enter the option from below\n 1.Push Operation\n 2.Pop Operation\n 3.Display\n Enter any key to Exit")
    str = input()
    if str == '1':
        print("Push Operation")
        push()
    elif str == '2':
        print("Pop Operation")
        pop()
    elif str == '3':
        print("Display Operation")
        display()
    else:
        print("Exit From Program")
        break





