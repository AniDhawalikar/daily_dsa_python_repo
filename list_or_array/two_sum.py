# input  :  arr = [0, -1, 2, -3, 1],  target = -2
# output : True

# [Naive Approach] Generating all Possible Pairs - O(n2) time and O(1) space
def calculate_sum(arr, target):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False



arr = [0, -1, 2, -3, 1]
target = -2
print(calculate_sum(arr, target))




# [Expected Approach] Using Hash Set - O(n) time and O(n) space
# Step By Step Implementations:

# Create an empty Hash Set or Unordered Set
# Iterate through the array and for each number in the array:
# => Calculate the complement (target - current number).
# => Check if the complement exists in the set:
# - If it is, then pair found.
# - If it isn’t, add the current number to the set.
# If the loop completes without finding a pair, return that no pair exists.


my_set = set()
def cal_sum(arr, target):
    for i in arr:
        compliment = target - i
        print(compliment)
        if compliment in my_set:
            return True
        my_set.add(i)
    return False


print(cal_sum(arr,target))