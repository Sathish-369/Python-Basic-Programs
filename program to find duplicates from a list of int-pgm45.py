

def Repeat(x):
    _size=len(x)
    repeated=[]
    for i in range(_size):
        k =i+1
        for j in range(k,_size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

list=[10,20,30,40,50,60,70,80,70,60,50,40,30,20,10,30,40,50,60,]
print(Repeat(list))
