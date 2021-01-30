

def largest(arr, n):

    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10,30,20,50,559]
n = len(arr)
ans = largest(arr, n)
print("Largest in given array is", ans)
