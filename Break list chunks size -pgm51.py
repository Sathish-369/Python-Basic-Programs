
my_list = ['sat','sat','ab', 'ab', 'am', 'am', 'sasa', 'sasa', 'susu', 'satsa']

def divide_chunks(l,n):

    for i in range (0, len(l), n):
        yield l[i:i + n]

n = 5
x = list(divide_chunks(my_list, n))
print(x)
