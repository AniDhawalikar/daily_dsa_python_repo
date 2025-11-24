# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , 
# the task is to return the elements in the intersection of the two arrays in sorted order.
# Intersection of two arrays can be defined as the set containing distinct common elements that 
# are present in both of the arrays.
# Examples:
# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
# Output: 1 2 3
# Explanation: Distinct elements in both the arrays are: 1 2 3.


def intersection(num1, num2):
    res = set(num1) & set(num2)
    return sorted(res)


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
print(intersection(a,b))

