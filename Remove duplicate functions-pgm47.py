

def remove_duplicates(list):
    list1=[]
    for item in list:
        if item not in list1:
            list1.append(item)
            return list1
        print(remove_duplicates([1,2,3,4,5,6,7]))
