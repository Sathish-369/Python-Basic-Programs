
def simple_interest(p,t,r):
    print("The principal is", p)
    print("The time period is", t)
    print("the rate of interest is", r)

    si=(p*t*r)/100

    print("The simple interest is", si)
    return si

simple_interest(100,10,10)