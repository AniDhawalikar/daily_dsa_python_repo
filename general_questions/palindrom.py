# input : n = "abba"
# output : True

# input : n = "ab"
# output : False


def check_palindrome(s):
    length = len(s)
    i = 0
    j = length-1

    while i < j:
        if s[i] != s[j]:
            return False
        return True
    
n = "121"
print(check_palindrome(n))
