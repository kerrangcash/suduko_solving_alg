import numpy as np

board = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,0]]

#determines if a sqaure is empty
def isEmpty(y,x):
    if board[y][x] == 0:
        return True
    else:
        return False

#determines if a given number can possibly fit in a square
def isSuitable(y,x,n):
    for i in range(0,9):
        if board[y][i] == n:
            return False
    for i in range(0,9):
        if board[i][x] == n:
            return False
    #finds the number square on a 3x3 section of board
    rootx = (x // 3) * 3
    rooty = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if board[rooty+i][rootx+j] == n:
                return False
    return True

#solve utilises isEmpty and isSuitable to find suitable numbers for empty squares
#and uses recursion to backtrack when no number is suitable
def solve():
    for y in range(9):
        for x in range(9):
            if isEmpty(y,x):
                for n in range(1,10):
                    if isSuitable(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print(np.matrix(board))

solve()
