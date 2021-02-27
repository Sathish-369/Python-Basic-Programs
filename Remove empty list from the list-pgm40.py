


list = [3,4,[],55,[],6,7,8,[]]
print("The original list is : " +str(list))

res = [ele for ele in list if ele !=[]]
print("list after empty list removel:"+str(res))
