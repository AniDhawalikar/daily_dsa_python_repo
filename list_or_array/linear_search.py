# linear search implementation 


def linear_search(arr, target):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return arr[i]
    return -1


nums = [1,2,3,4,5,6,7,8,9]
k = 11
print(linear_search(nums, k))
