def take_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix
def multiply_matrices(X, Y):

    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    return result

if __name__ == "__main__":
    r1 = int(input("Enter the number of rows for matrix X: "))
    c1 = int(input("Enter the number of columns for matrix X: "))
    
    r2 = int(input("Enter the number of rows for matrix Y: "))
    c2 = int(input("Enter the number of columns for matrix Y: "))

    if c1 != r2:
        print("Matrix multiplication is not possible. Columns of X must equal rows of Y.")
    else:
        print("Enter elements for matrix X:")
        X = take_matrix_input(r1, c1)
        
        print("Enter elements for matrix Y:")
        Y = take_matrix_input(r2, c2)

        result = multiply_matrices(X, Y)

        print("The result of multiplying matrices X and Y is:")
        for r in result:
            print(r)
