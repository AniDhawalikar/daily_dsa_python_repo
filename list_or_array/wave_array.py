# Given an sorted array arr[] of integers. Sort the array into a wave-like array(In Place). 
# In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5] ..... and so on. 
# If there are multiple solutions, find the lexicographically smallest one.

# Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

def wave_array(arr):
    n = len(arr)
    i = 0 
    j = i + 1

    while j < n:
        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 2
    return arr

nums = [1, 2, 3, 4, 5]
print(wave_array(nums))

