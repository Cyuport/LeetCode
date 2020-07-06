def maximalSquare(matrix: [[str]]) -> int:
    row = len(matrix)
    if row == 0:
        return False
    col = len(matrix[0])
    size = 0
    queue = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '1':
                queue.append([i, j])
    length = len(queue)
    while length:
        size += 1
        for k in range(length):
            i, j = queue.pop(0)
            if i + size == row or j + size == col:
                continue
            flag = True
            for a in range(i, i + size + 1):
                if matrix[a][j + size] == '0':
                    flag = False
                    break
            if not flag:
                continue
            for b in range(j, j + size + 1):
                if matrix[i + size][b] == '0':
                    flag = False
                    break
            if not flag:
                continue
            queue.append([i, j])
        length = len(queue)
    return size**2


if __name__ == '__main__':
    print(maximalSquare([['1','0','1','1','1'],
                         ['1','0','1','1','1'],
                         ['1','1','1','1','1'],
                         ['1','0','0','1','0']
                        ]))