# input : n = "ab"
# output : 4...(a,b,ab,ba)


my_set = set()

def count_distinct_string(n):
    for i in range(0,len(n)):
        str = ""
        for j in range(i, len(n)):
            str+=n[i]
            my_set.add(str)
    return len(my_set)+1
 

n = "ab"
print(count_distinct_string(n))
