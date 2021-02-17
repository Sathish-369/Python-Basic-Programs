

list = [22,33,14,53,67,55,42,46,88,77]
even_nos = [num for num in list if num % 2 == 0]
print("Even number in the list:", even_nos)

# Using for loop:

list = [22,33,14,53,67,55,42,46,88,77]

for  num in list:
    if num % 2 == 0:
        print(num, end = " ")


# Using while loop:

list = [22,33,14,53,67,55,42,46,88,77]
num = 0

while(num < len(list)):
    if num % 2 == 0:
        print(list[num], end = "  ")
    num +=1

