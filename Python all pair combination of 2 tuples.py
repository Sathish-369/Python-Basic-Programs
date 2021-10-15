
from itertools import chain, product

test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

print("the original tuples 1 :" + str(test_tuple1))
print("the original tuple 2 : " + str(test_tuple2))

res = list(chain(product(test_tuple1, test_tuple2), product(test_tuple2, test_tuple1)))
print("the filtered tuples :"+str(res))