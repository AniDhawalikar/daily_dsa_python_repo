# longest sequence 


# Brute force Approach [O(n**2)]
def find_sequence(arr):
    n = len(arr)
    max_count = 0
    for i in range(n):
        num = arr[i]
        count = 1
        while num + 1 in arr:
            count += 1
            num = num +1

        max_count = max(max_count, count)

    return max_count


nums = [1,99,101,98,2,5,3,100,1,1]
print(find_sequence(nums))


# Better Approach [O(n*log(n))]
def find_sequence1(arr):
    last_smaller = float("-inf")
    count = 1
    longest = 0
    arr.sort()
    for i in range(0,len(arr)):
        num = arr[i]
        if num - 1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            count = 1
            last_smaller = num
        longest = max(longest, count)
    return longest

print(find_sequence1(nums))


# Optimal Approach [O(n)]
def find_sequence2(arr):

    set_arr = set()
    count = 0
    longest = 0

    for i in range(0, len(arr)):
        set_arr.add(arr[i])

    for i in set_arr:
        if i - 1 not in set_arr:
            num = i
            count = 1
            while num + 1 in set_arr:
                count += 1
                num += 1
            longest = max(longest, count)
    return longest

print(find_sequence2(nums))
