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
        i += 1
        j -= 1
    return True
    
n = "abaa"
print(check_palindrome(n))
