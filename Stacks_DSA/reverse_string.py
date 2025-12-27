def reverse(str):
    list = []
    for char in str:
        list.append(char)
    return list[::-1]

str = input("Enter a String :  ")
reverse_str = "".join(reverse(str))
print("Reverse of Entered String :  ",reverse_str)