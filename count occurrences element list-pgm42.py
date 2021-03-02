

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = [3,4,5,6,7,8,8,99,90,80]
x = 8
print("{} has occurred {} times" .format(x, countX(lst, x)))