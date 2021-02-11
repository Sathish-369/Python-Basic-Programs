


list1 =[1,2,33,4,4,55,5]

def sumofList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size -1] + sumofList(list, size -1)

total = sumofList(list1, len(list1))
print("Sum of list: ", total)



