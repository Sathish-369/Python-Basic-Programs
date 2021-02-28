

def cloning(list):
    li_copy = list[:]
    return li_copy

list = [2,3,44,55,6,7,8]
list1 = cloning(list)
print("Original list: ", list1)
print("Cloning list: ", list1)