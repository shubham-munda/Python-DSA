def parenthesis_checker(s):
    stack = []
    pairs = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]" : 
            if not stack:
                return False
            top = stack.pop()
            if pairs[char] != top:
                return False

    return len(stack) == 0    
s = input("Enter :  ")
checker = parenthesis_checker(s)
if checker:
    print("All Brackets are well formed.")
else:
    print("Brackets are not well formed.")