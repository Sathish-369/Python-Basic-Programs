
# using list comprehension:

list1 = [23,34,45,56,67,78,89,90]
only_odd = [num for num in list1 if num % 2 == 1]
print(only_odd)

# Using for loop:

list1 = [23,34,45,56,67,78,89,90]

for num in list1:
    if num % 2 != 0:
        print(num, end = " ")