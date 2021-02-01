

def reversalArray(arr, start, end):
    while(start < end):
        temp = arr [start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end -1

def leftrotate(arr, d):
    n = len(arr)
    reversalArray(arr, 0, d-1)
    reversalArray(arr, d, n-1)
    reversalArray(arr, 0, n-1)

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

arr = [1,2,3,4,5,6,7]
leftrotate(arr, 2)
printArray(arr)
