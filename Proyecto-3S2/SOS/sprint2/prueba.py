def check_rows(board):
    size = len(board)
    for i in range(size):
        for j in range(size-2):
            if board[i][j] == 'S' and board[i][j + 1] == 'O' and board[i][j + 2] == 'S':
                print(i,j,j+1,j+2)
                return True

    for i in range(size-2):
        for j in range(size):
            if board[i][j] == 'S' and board[i + 1][j] == 'O' and board[i + 2][j] == 'S':
                print(i,j,i+1,i+2)
                return True

    for i in range(size-2):
        for j in range(size-2):
            if board[i][j] == 'S' and board[i+1][j+1] == 'O' and board[i+2][j+2] == 'S':
                print(i, j,i+1,j+1,i+2,j+2)
                return True

    for i in range(2, size):
        for j in range(size-2):
            if board[i][j] == 'S' and board[i-1][j+1] == 'O' and board[i-2][j+2] == 'S':
                print(i, j,i-1,j+1,i-2,j+2)
                return True

    return False

board=[['S', 'S', 'S', 'S'],
       [None, 'S', 'S', None],
       [None, 'O', None, None],
       ['S', None, None, 'S']]
if check_rows(board):
    print('win')
else:
    print('lose')
