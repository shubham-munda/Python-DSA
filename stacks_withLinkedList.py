class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,value):
        New_Node = Node(value)
        if self.head :
            New_Node.next = self.head
        self.head = New_Node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError ("Stack is Empty.")
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            raise IndexError ("Stack is Empty.")
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stack_size(self):
        return self.size
    
    def traverse_and_print(self):
        current_node = self.head
        while current_node:
            print(current_node.value ,end="->")
            current_node = current_node.next
        print()

def input_operation():
    print("Press 1 for 'Push Operation'\nPress 2 for 'Pop Operation'\nPress 3 for 'Peek Element'")
    print("Press 4 for 'Stack Length'\nPress 5 for 'Checking Empty Stack'")
    print("------------------------------------------------------------------------")
    
def input_num():
    number = int(input("Which Stack operation do you wish to perform :  "))
    return number

obj  = Stack()
input_operation()
num = input_num()

main_check = 1
while(main_check):
    if (num == 1):
        element = int(input("Enter Number :  " ))
        obj.push(element)
        print("------------------------------------")
    elif (num == 2):
        obj.pop()
        print("Stack Element : ", end="")
        obj.traverse_and_print()
        print("------------------------------------")
    elif (num == 3):
        peek_num = obj.peek()
        print("Peek Number : ",peek_num)
        print("------------------------------------")
    elif (num == 4):
        length = obj.stack_size()
        print(f"Length of the Stack : {length}")
        print("------------------------------------")
    elif (num == 5):
        is_empty = obj.isEmpty()
        print("Stack is Empty : ",is_empty)
        print("------------------------------------")
    else :
        print("ERROR ! Try Again.")
        print("------------------------------------")

    main_check2 = 1
    while(main_check2):
        check = input("Perform Another Operation (Yes/No) : ")
        if check.lower() == 'yes' :
            num = input_num()
            main_check = 1
            main_check2 = 0
        elif check.lower() == 'no' :
            main_check = 0
            main_check2 = 0
        else :
            print("ERROR ! Try Again.")
            main_check2 = 1

print("------------------------------------------------------------------------")
print("Current Stack Elements : ", end="")
obj.traverse_and_print()
