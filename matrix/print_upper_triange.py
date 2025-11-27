# given input matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print the upper triangle of the matrix
# 1 2 3
# 4 5 6
# 7 8 9 
# for the above matrix we have to print the upper triangle elements.
# output like : 
# 1 2 3
# * 5 6
# * * 9


def print_upper_traingle(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if j >= i:
                print(arr[i][j], end = " ")
            else:
                print("*", end = " ")
        print()  


nums = [[1,2,3],[4,5,6],[7,8,9]]
print_upper_traingle(nums)
