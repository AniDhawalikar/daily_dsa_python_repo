# find Max Consecutive Ones occured in the given array.


def max_consecutive_ones(arr):
    n = len(arr)
    count = 0
    max_count = 0

    for i in range(0, n):
        if arr[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(count, max_count)

nums = [1,1,0,1,1,1,1,0,1,1,0,1,0]
print(max_consecutive_ones(nums))
