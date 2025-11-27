# given input matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print the transpose of the matrix
# 1 2 3
# 4 5 6
# 7 8 9 
# for the above matrix we have to print the transpose elements.
# output like : 
# 1 * *
# * 5 *
# * * 9


def print_transpose(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if i == j:
                print(arr[i][j], end = " ")
            else:
                print("*", end = " ")
        print()


nums = [[1,2,3],[4,5,6],[7,8,9]]
print_transpose(nums)

