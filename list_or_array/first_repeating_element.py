# Given an array arr[], find the first repeating element. 
# The element should occur more than once and the index of its first occurrence should be the smallest.
# Note:- The position you return should be according to 1-based indexing. 


def find_first_repeating_num(arr):
    my_dict = dict()
    n = len(arr)
    seen = False
    
    for i ,j in enumerate(arr):
        if j not in my_dict:
            my_dict[j] = i
        else:
            n = min(n, my_dict[j])
            seen = True
    
    if not seen:
        return -1
    return n + 1


nums = [1, 5, 3, 4, 3, 5, 6]
print(find_first_repeating_num(nums))
