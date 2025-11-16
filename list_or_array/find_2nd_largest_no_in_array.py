# find the 2nd largest number in the array

def second_largest_num(arr):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(arr)

    for i in range(0, n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]

        elif arr[i] > s_largest and arr[i] != largest:
            s_largest = arr[i] 

    return s_largest

nums = [-55, -2, -97, -99, -3, -76]
print(second_largest_num(nums))