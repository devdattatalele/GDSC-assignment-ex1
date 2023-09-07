rows1 = int(input("Enter the number of rows in the first matrix: "))
cols1 = int(input("Enter the number of columns in the first matrix: "))

matrix1 = []
print("Enter the elements of the first matrix:")
for i in range(rows1):
    row = [int(x) for x in input().split()]
    if len(row) != cols1:
        print(f"Row {i + 1} should have {cols1} elements.")
        exit()
    matrix1.append(row)

rows2 = int(input("Enter the number of rows in the second matrix: "))
cols2 = int(input("Enter the number of columns in the second matrix: "))

matrix2 = []
print("Enter the elements of the second matrix:")
for i in range(rows2):
    row = [int(x) for x in input().split()]
    if len(row) != cols2:
        print(f"Row {i + 1} should have {cols2} elements.")
        exit()
    matrix2.append(row)

if cols1 != rows2:
    print("Matrix multiplication is not possible. Columns of the first matrix must be equal to rows of the second matrix.")
    exit()

result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

print("Resultant Matrix:")
for row in result_matrix:
    print(" ".join(map(str, row)))
