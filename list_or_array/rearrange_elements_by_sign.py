# write a python code to update the given list in such a way that 
# we get the positive and negative numbers alternatly.
# store the new sqeuence in the list and return the respected list.


# brute force approach
def rearrange_elements(arr):
    pos = []
    neg = []
    n = len(arr)
    for i in range(0, n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(0, len(pos)):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]

    return arr


nums = [5,10,-3,-1,-10,6]
print(rearrange_elements(nums))



# optimal approach
def rearrange_elements_optimal(arr):
    n = len(arr)
    result = [0]*n
    pos_index = 0
    neg_index = 1
    for i in range(0, n):
        if arr[i] >= 0:
            result[pos_index] = arr[i]
            pos_index += 2
        else:
            result[neg_index] = arr[i]
            neg_index += 2

    return result


print(rearrange_elements_optimal(nums))