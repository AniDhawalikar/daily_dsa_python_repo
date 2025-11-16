# check that array is sorted or not

def check_array(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

nums = [1,2,3,4,5,6,7,8,90]
print(check_array(nums))