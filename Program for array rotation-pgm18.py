

def leftrotate(arr, d, n):
    for i in range(d):
        leftrotatebyOne(arr, n)

def leftrotatebyOne(arr, n):
    temp = arr[0]
    for i in range (n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr, size):
    for i in range(size):
        print("%d"% arr[i], end="")

arr= [1,2,3,4,5,6,7,8,9]
leftrotate(arr, 2, 9)
printArray(arr, 6)
