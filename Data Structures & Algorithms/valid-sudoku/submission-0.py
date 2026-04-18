class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(len(board))]
        squares = [set() for _ in range(len(board))]
        for r in range(len(board)):
            row = set()
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    # check for valid or invalid rows
                    if board[r][c] in row:
                        return False
                    else:
                        row.add(board[r][c])
                
                    # check for valid or invalid columns
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                
                if board[r][c] != "." and r < 3 and c < 3:
                    if board[r][c] in squares[0]:
                        return False
                    else:
                        squares[0].add(board[r][c])
                elif board[r][c] != "." and r < 3 and c >= 3 and c < 6:
                    if board[r][c] in squares[1]:
                        return False
                    else:
                        squares[1].add(board[r][c])
                elif board[r][c] != "." and r < 3 and c >= 6 and c < 9:
                    if board[r][c] in squares[2]:
                        return False
                    else:
                        squares[2].add(board[r][c])
                elif board[r][c] != "." and r >= 3 and r < 6 and c < 3:
                    if board[r][c] in squares[3]:
                        return False
                    else:
                        squares[3].add(board[r][c])
                elif board[r][c] != "." and r >= 3 and r < 6 and c >= 3 and c < 6:
                    if board[r][c] in squares[4]:
                        return False
                    else:
                        squares[4].add(board[r][c])
                elif board[r][c] != "." and r >= 3 and r < 6 and c >= 6 and c < 9:
                    if board[r][c] in squares[5]:
                        return False
                    else:
                        squares[5].add(board[r][c])
                elif board[r][c] != "." and r >= 6 and r < 9 and c < 3:
                    if board[r][c] in squares[6]:
                        return False
                    else:
                        squares[6].add(board[r][c])
                elif board[r][c] != "." and r >= 6 and r < 9 and c >= 3 and c < 6:
                    if board[r][c] in squares[7]:
                        return False
                    else:
                        squares[7].add(board[r][c])
                elif board[r][c] != "." and r >= 6 and r < 9 and c >= 6 and c < 9:
                    if board[r][c] in squares[8]:
                        return False
                    else:
                        squares[8].add(board[r][c])

        
        return True