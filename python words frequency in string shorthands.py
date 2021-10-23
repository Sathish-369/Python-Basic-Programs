test_str = 'star is best . Sats are good and Sats like star'

print("the original string is : " + str(test_str))

res = {key: test_str.count(key) for key in test_str.split()}

print("the words frequency:"+str(res))