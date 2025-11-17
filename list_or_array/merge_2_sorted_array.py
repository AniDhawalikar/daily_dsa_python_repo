# merge 2 sorted lists into single list without adding duplicate elements

def merge_2_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    result_arr = []
    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if len(result_arr) == 0 or result_arr[-1] != arr1[i]:
                result_arr.append(arr1[i])
            i += 1
        else:
            if len(result_arr) == 0 or result_arr[-1] != arr2[j]:
                result_arr.append(arr2[j])
            j += 1

    while i < n :
        if len(result_arr) == 0 or result_arr[-1] != arr1[i]:
            result_arr.append(arr1[i])
        i += 1

    while j < m :
        if len(result_arr) == 0 or result_arr[-1] != arr2[j]:
            result_arr.append(arr2[j])
        j += 1

    return result_arr

nums1 = [1,2,3]
nums2 = [4,5,6]
print(merge_2_arrays(nums1, nums2))

