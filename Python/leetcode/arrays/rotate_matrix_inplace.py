def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):   # Note: starts from "i", not "0"
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    return matrix
