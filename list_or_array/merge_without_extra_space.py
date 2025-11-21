# Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. 
# Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.
# Examples:
# Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
# Output: a[] = [2, 2, 3, 4], b[] = [7, 10]
# Explanation: After merging the two non-decreasing arrays, we get, [2, 2, 3, 4, 7, 10]


def mergeArrays(a, b):
    # code here
    c = a + b
    c.sort()
    
    
    for i in range(len(a)):
        a[i] = c[i]
        
    for i in range(len(a), len(c)):
        b[i-len(a)] = c[i]
        
    return a, b