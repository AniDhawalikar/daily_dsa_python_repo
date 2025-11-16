# find maximum number from given array

def find_max(arr):
    largest = float("-inf")
    n = len(arr)
    for i in range(0, n):
        largest  = max(largest, arr[i])
    
    return largest


nums = [55, 32, -97, 99, 3, 76]
print(find_max(nums))