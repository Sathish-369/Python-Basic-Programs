
def sum(mydict):
    sum =0
    for i in mydict:
        sum=sum+mydict[i]

    return sum
dict={'a':100,'b':200,'c':500}
print('sum :', sum(dict))