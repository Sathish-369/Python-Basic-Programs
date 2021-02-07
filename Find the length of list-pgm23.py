
from operator import length_hint

test_list = [1,2,4,6,7,9]
print("the list is: "+str(test_list))

list_len = len(test_list)

list_len_hint = length_hint(test_list)

print("Length of list is: " + str(list_len))
print("List of list using length_hint() is : "+ str(list_len_hint))