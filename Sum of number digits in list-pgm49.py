

list = [12,23,34,45,56,67,78]

print('list is : '+ str(list))

res=[]
for ele in list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)

print( " Summation: "+ str(res))
