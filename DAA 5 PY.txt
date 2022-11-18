import numpy as np

def main():
    global n
    n = input("Enter N: ")
    n = int(n)
    global board
    board = np.zeros((n,n), dtype=int)
    solve_board()

def print_board():
    print('-'*n)
    for row in board:
        for col in row:
            if col == 1:
                print ("Q", end = " ")
            else:
                print (".", end = " ")
        print()



def is_valid(board,i,j,n): 

    if 1 in board[i]: #Checking row
        return False

    for row in range(0, n): #Checking column
        if (board[row][j]==1):
            return False 

    for k in range(0,n): #Checking Diagonal
        for l in range(0,n):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return False
    return True

def solve_board():
    for row in range(n):
        for col in range(n):
            if board[row][col] == 0: #no queen
                if (is_valid (board,row,col,n)):
                    board[row][col] = 1 #Assigning 1 for queen
                    if np.count_nonzero(board) == n:
                      print_board()
                      return True
                    solve_board()
                    board[row][col] = 0
            else:
                  return False

if __name__ == "__main__":
    main()

