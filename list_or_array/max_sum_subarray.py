# find the maximum sum of the subarray from the given array


# brute force solution
def max_sum_array(arr):
    max_num = float("-inf")
    n = len(arr)
    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            max_num = max(max_num, total)
        
    return max_num

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sum_array(nums))


# optimal solution
def max_sum_array1(arr):
    n = len(arr)
    max_num = float("-inf")
    total = 0
    for i in range(0, n):
        total += arr[i]
        max_num = max(max_num,total)
        if total < 0 :
            total = 0
    return max_num
 
print(max_sum_array1(nums))    