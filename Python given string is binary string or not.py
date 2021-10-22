def check(string) :

    p = set(string)

    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        print("yes")

    else:
        print("no")

if __name__=="__main__":
    string = "10101000001111"

    check(string)