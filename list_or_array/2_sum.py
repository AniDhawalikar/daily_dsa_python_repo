# write a function in the python which is giving the index of the array elements whoes sum is equal to the given input sum.
# if sum is not present return -1

def two_sum(arr, s):
    freq = dict()
    n = len(arr)
    for i in range(0,n):
        if (s - arr[i]) in freq:
            return [i, freq[s - arr[i]]]
        freq[arr[i]] = freq.get(arr[i], i)


nums = [5,9,1,2,4,15,6,3]
k = 13
print(two_sum(nums, k))
