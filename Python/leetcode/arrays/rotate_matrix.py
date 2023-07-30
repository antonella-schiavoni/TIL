def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    result = []
    for i in range(len(matrix)):
        final_row = []
        for row in matrix:
            final_row.append(row[i])
        result.append(final_row)
    print(result)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
