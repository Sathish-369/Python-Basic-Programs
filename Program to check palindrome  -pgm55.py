

def isPalindrome(s):
    return s == s[::-1]
s = "satas"
ans = isPalindrome(s)
print(s)
if ans:
    print("yes")
else:
    print("no")