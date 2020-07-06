def gameOfLife(board: [[int]]) -> [[int]]:
    row, col = len(board), len(board[0])
    for i in range(row):
        for j in range(col):
            count = 0
            if i != 0 and board[i-1][j] > 0:
                count += 1
            if j != 0 and board[i][j-1] > 0:
                count += 1
            if i != row-1 and board[i+1][j] > 0:
                count += 1
            if j != col-1 and board[i][j+1] > 0:
                count += 1
            if i != 0 and j != 0 and board[i-1][j-1] > 0:
                count += 1
            if i != 0 and j != col-1 and board[i-1][j+1] > 0:
                count += 1
            if i != row-1 and j != 0 and board[i+1][j-1] > 0:
                count += 1
            if i != row-1 and j != col-1 and board[i+1][j+1] > 0:
                count += 1
            if board[i][j] == 0 and count == 3:
                board[i][j] = -1
            if board[i][j] == 1:
                if count < 2 or count > 3:
                    board[i][j] = 2
    for i in range(row):
        for j in range(col):
            if board[i][j] == -1:
                board[i][j] = 1
            elif board[i][j] == 2:
                board[i][j] = 0
    return board


if __name__ == '__main__':
    print(gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))
