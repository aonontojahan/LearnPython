
def take_matrix_input():

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []

    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix, rows, cols

def display_matrix(matrix):
    print("The matrix is:")
    for row in matrix:
        print(row)

matrix, rows, cols = take_matrix_input()
display_matrix(matrix)
print(f"Matrix dimensions: {rows}x{cols}")