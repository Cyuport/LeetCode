def setZeroes(matrix: [[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    row, col = [0]*m, [0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(m):
        if row[i] == 1:
            for j in range(n):
                matrix[i][j] = 0
        else:
            for j in range(n):
                if col[j] == 1:
                    matrix[i][j] = 0

def setZeroes2(matrix: [[int]]) -> None: #用第一行和第一列记录信息，避免O（n）空间复杂度
    first_row, first_col = False, False
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        if matrix[i][0] == 0:
            first_col = True
            break
    for j in range(n):
        if matrix[0][j] == 0:
            first_row = True
            break
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
        else:
            for j in range(1,n):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
    if first_col:
        for i in range(m):
            matrix[i][0] = 0
    if first_row:
        for j in range(n):
            matrix[0][j] = 0



