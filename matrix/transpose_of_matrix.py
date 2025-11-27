# given input matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print the transpose of the matrix
# 1 2 3
# 4 5 6
# 
# for the above matrix we have to print the transpose.
# output like : 
# 1 4 
# 2 5 
# 3 6 


def transpose_matrix(arr):
    rows = len(arr)
    cols = len(arr[0])

    result = [[0]*rows for _ in range(cols)]     
    # use list comprhensions for making [[0,0],[0,0],[0,0]] to store the result after transpose

    for i in range(0,rows):
        for j in range(0,cols):
            result[j][i] = arr[i][j]
    return result
        


nums = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose_matrix(nums))

