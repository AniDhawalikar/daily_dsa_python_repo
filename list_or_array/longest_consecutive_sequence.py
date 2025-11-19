# write a python code to find out longest consecutive sequence present in the array


# brute force solution
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


# 