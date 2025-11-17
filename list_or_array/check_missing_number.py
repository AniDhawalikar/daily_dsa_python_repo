# write a code in python to find out the missing number from the given array and return these numbers as output
# input n = [1.2,3,0,5]
# output = 4


# General Approach
def check_missing_number(arr):
    n = max(arr)
    i = 0
    result = []
    while i < n:
        if i not in arr:
            result.append(i)
        i += 1
    return result

nums = [1,2,3,0,5]
print(check_missing_number(nums))



# Better Approach
def check_missing_number_better(arr):
    n = len(arr)
    freq = dict()
    for i in range(0, n+1):
        freq[i] = 0

    for i in arr:
        freq[i] = 1
    
    for i, j in freq.items():
        if j == 0:
            return i
        
print(check_missing_number_better(nums))



# Optimal Approach
def check_missing_number_optimal(arr):
    n = len(arr)
    sum = 0
    for i in arr:
        sum += i

    diff = ((n*(n+1))//2) - sum

    if diff > 0:
        return diff

print(check_missing_number_optimal(nums))
