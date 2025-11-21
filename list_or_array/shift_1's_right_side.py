# Given an array arr consisting of only 0's and 1's in random order. 
# Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.
# Input: arr[] = [0, 0, 1, 1, 0]
# Output: [0, 0, 0, 1, 1]
# Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].

def shift_array(arr):
    n = len(arr)
    i = 0

    if n == 1:
        return arr
    
    # findout 1st 1 in the array
    while i < n:
        if arr[i] == 1:
            break
        i += 1

    # if i is not there in the array then return the array as it is.
    if i == n :
        return arr
    
    # now move j index ahead of i index till getting the non 1 element.
    # after geeting that element swap that with 0.
    # so that we get 1 on right side and zeros on left side.
    j = i + 1
    while j < n:
        if arr[j] != 1:
            arr[i], arr[j] == arr[j], arr[i]
            i += 1
        j += 1
    return arr

nums = [0, 0, 1, 1, 0]
print(shift_array(nums))