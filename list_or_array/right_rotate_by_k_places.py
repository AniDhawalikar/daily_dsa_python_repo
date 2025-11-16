# right rotate an array by k places

def reverse_array(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def right_rotate(arr, k):
    n = len(arr)
    reverse_array(arr, n-k, n-1)
    reverse_array(arr, 0, n-k-1)
    reverse_array(arr, 0, n-1)
    return arr

nums = [1,2,3,4,5,6,7,8,9]
k = 5
print(right_rotate(nums, k))

