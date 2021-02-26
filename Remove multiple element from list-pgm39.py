

list = [22,44,3,4,5,6,7,8,99]

del list [2:4]
print(list)

# Using list comprehension(Remove even numbers):

list = [22,44,3,4,5,6,7,8,99]
list = [elem for elem in list if elem % 2 !=0]
print(list)