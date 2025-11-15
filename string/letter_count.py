# input  : n = "aaabbbbccddddaaaabbbccc"
# Output : a3b4c2d4a4b3c3

def count_string_letters(s):
    if not s:
        return ""

    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1

    # Append last character group
    result.append(s[-1] + str(count))

    return "".join(result)


n = "abbbcccaaaabbbcccwwweerrrtt"
print(count_string_letters(n))

