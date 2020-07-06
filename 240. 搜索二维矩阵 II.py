def searchMatrix(matrix: [[int]], target: int) -> bool:
    row = len(matrix)
    if row == 0:
        return False
    col = len(matrix[0])
    i, j = row - 1, 0
    while i >= 0 and j < col:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
    return False


if __name__ == '__main__':
    print(searchMatrix([
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],20))

