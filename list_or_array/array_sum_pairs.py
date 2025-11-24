# Python3 program to find all 
# pair in both arrays whose 
# sum is equal to given value x


my_set = set()
def find_pairs(arr1, arr2, target):
    for i in arr1:
        my_set.add(i)
    
    for j in arr2:
        if (target - arr2[j]) in my_set:
            print ((target - j), j)
    return "Not Found"


arr1 = [1, 0, -4, 7, 6, 4]
arr2 = [0, 2, 4, -3, 2, 1]
target = 8
find_pairs(arr1, arr2, target)





