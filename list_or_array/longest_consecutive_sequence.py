# write a python code to find out longest consecutive sequence present in the array


# brute force solution
# Itrate through out the array and find the next number of current element is present in the array or not.
# if present then count increases if not then count will be 0 and again shift the ith index on the next element.
# and finally compare the cout with the max count and return the count. 

def longest_sequence(arr):
    n = len(arr)
    max_count = 0

    for i in range(0,n):
        num = arr[i]
        count = 1
        while num+1 in arr:
            count += 1
            num += 1
            max_count = max(max_count, count)
    return max_count


nums = [1,99,101,98,2,5,3,100,1,1]
print(longest_sequence(nums))


# Better solution
# Initially sor the given array.
# then check all the elements one by one. if the elements are present in the sequence then simply increases the count.
# else count again initialize to 1 and repeat the process ahead.

def longest_sequence_better(arr):
    n = len(arr)
    arr.sort()
    longest = 0
    last_smaller = float("-inf")
    count = 0

    for i in range(0,n):
        if arr[i] == last_smaller + 1:
            last_smaller = arr[i]
            count += 1 
        else:
            last_smaller = arr[i]
            count = 1

        longest = max(count, longest)

    return longest

print(longest_sequence_better(nums))


# optimal approach
# we are going to iterate through the array and put all the elements in to the set.
# so we get all the unique elements.
# then one by one check that the next element is present in the set or not.
# if present then increase the count otherwise count initialize to 1 again.
# note : here we first check that if there privious element is present in the set or not.
# if present then move to the next number else check the sequence.

def longest_sequence_optimal(arr):
    n = len(arr)
    myset = set()
    for i in range(0, n):
        myset.add(arr[i])
    
    count = 0
    longest = 0
    for i in myset:
        if i- 1 not in myset:
            num = i
            count = 1 
            while num + 1 in myset:
                count +=1
                num += 1
            longest = max(longest, count)

    return longest

print(longest_sequence_optimal(nums))
