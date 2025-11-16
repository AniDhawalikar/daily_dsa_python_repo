# remove duplicates from the array of elements

def remove_duplicates(arr):
    n = len(arr)
    if n == 1:
        return 1
    i = 0
    j =i+1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return i + 1


nums = [1,1,1,2,3,4,4,7,9,9,9,10]
print(remove_duplicates(nums))

