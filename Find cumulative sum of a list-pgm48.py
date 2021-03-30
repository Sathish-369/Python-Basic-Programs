def cumulative(list):
    cu_list=[]
    length = len(list)
    cu_list = [sum(list[0:x:1])for x in range(0, length+1)]
    return cu_list[1:]

list=[10,20,30,40,50,60,70]
print(cumulative(list))