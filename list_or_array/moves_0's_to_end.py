# moves zeros to the end of the array/list

def move_zeros_at_end(arr):
    n = len(arr)
    i = 0
    j = i + 1

    # If single element, return as is
    if n == 1:
        return arr

    # Find first zero
    while i < n:
        if arr[i] == 0:
            break
        i += 1

    # If no zero found, return array
    if i == n:
        return arr

    # Swap zeros with next non-zero
    j = i + 1
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    return arr

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
print(move_zeros_at_end(nums))
