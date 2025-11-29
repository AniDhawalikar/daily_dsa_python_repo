# we are getting a matrix which contains 0's.
# we need to traverse throughout the matrix, then find out the zeros then,
# mark all the elements as a 0 in the respective column and row.
# 1 2 3 5       1 0 0 5
# 4 5 0 8   ==> 0 0 0 0
# 7 0 9 3       0 0 0 0 
# 6 9 3 2       6 0 0 2
# input     ==> output


def set_matrix_to_zero(arr):
    r = len(arr)
    c = len(arr[0])

    r_track = [0 for _ in range(0, r)]
    c_track = [0 for _ in range(0, c)]

    for i in range(0, r):
        for j in range(0, c):
            if arr[i][j] == 0:
                r_track[i] = -1
                c_track[j] = -1

    for i in range(0, r):
        for j in range(0, c):
            if r_track[i] == -1 or c_track[j] == -1:
                arr[i][j] = 0

    return arr

nums = [[1,2,3,4],[4,5,0,8],[7,0,9,3],[6,9,3,2]]
print(set_matrix_to_zero(nums))

