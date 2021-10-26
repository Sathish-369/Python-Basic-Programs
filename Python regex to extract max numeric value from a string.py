import re
def extractmax(input):

    numbers = re.findall('\d+',input)
    numbers = map(int,numbers)
    print (Max(numbers))
if __name__=="__main__":
    input = '200sat564abi444gg'
    extractMax(input)