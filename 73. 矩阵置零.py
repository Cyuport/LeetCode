def setZeroes(matrix: [[int]]):
    row, col = len(matrix), len(matrix[0])
    flag_r, flag_c = False, False
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                if i:
                    matrix[i][0] = 0
                else:
                    flag_r = True
                if j:
                    matrix[0][j] = 0
                else:
                    flag_c = True
    for i in range(1, row):
        if matrix[i][0] == 0:
            matrix[i] = [0 for _ in range(col)]
    for j in range(1, col):
        if matrix[0][j] == 0:
            for i in range(row):
                matrix[i][j] = 0
    if flag_r:
        matrix[0] = [0 for _ in range(col)]
    if flag_c:
        for i in range(row):
            matrix[i][0] = 0
    return matrix

if __name__ == '__main__':
    print(setZeroes([[1,1,1],[0,1,2]]))