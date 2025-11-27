# print the matrix as per the user inputs.


print("Enter how many rows are there in the matrix : ")
rows = int(input("Enter rows : "))

print("Enter how many cols are there in the matrix : ")
cols = int(input("Enter cols : "))

matrix = []

for i in range(0, rows):
    a = []
    for j in range(0, cols):
        p = int(input(f"Enter {i,j} matrix elements :"))
        a.append(p)
    matrix.append(a)    


for i in range(0, rows):
    for j in range(0, cols):
        print(matrix[i][j], end=" ")
    print()
