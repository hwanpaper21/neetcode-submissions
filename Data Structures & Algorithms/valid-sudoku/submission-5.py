class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lst_row = []
        col_row = []
        box = []
        x = 9
        y = 3
        m = 0
        n = 0
        for i in range (9):
            for j in board[i]:
                if j != ".":
                    if j not in lst_row:
                        lst_row.append(j)
                    else:
                        return False
            lst_row = []
        
        for k in range(9):
            for l in range(9):
                if board[l][k] != ".":
                    if board[l][k] not in col_row:
                        col_row.append(board[l][k])
                    else:
                        return False
            col_row = []

        while m < 9:
            for n in range(y):
                if board[n][m] != ".":
                    if board[n][m] not in box:
                        box.append(board[n][m])
                    else:
                        return False
                if m % 3 == 2 and n % 3 == 2:
                    box = []
                    print ("cleared")
            m += 1

        m = 0
        while m < 9:
            for n in range(6):
                if board[n][m] != "." and n > 2:
                    print((m,n,x,y))
                    if board[n][m] not in box:
                        box.append(board[n][m])
                    else:
                        return False
                if m % 3 == 2 and n % 3 == 2:
                    box = []
                    print ("cleared")
            m += 1
        m = 0

        while m < 9:
            for n in range(9):
                if board[n][m] != "." and n > 5:
                    print((m,n,x,y))
                    if board[n][m] not in box:
                        box.append(board[n][m])
                    else:
                        return False
                if m % 3 == 2 and n % 3 == 2:
                    box = []
                    print ("cleared")
            m += 1
            
    
 

    
       

        return True