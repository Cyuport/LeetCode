def rotate(matrix:[[int]])->None:
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


if __name__ == '__main__':
    matrix = [[1,2,3],
  [4,5,6],
  [7,8,9]]
    rotate(matrix)
    print(matrix)