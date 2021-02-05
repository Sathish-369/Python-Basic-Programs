

def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size -1] = temp

    return  newList

newList = [12,45.67,89,98]
print(swapList(newList))