class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack.copy()


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
        print(f"Stack Element : {obj.display()}")
        print("------------------------------------")
    elif (num == 3):
        peek_num = obj.peek()
        print("Peek Number : ",peek_num)
        print("------------------------------------")
    elif (num == 4):
        length = obj.size()
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
print("Current Stack Elements :  ",obj.display())