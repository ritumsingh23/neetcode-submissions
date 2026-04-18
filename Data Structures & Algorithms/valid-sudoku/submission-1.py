class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            row = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Row check
                if val in row:
                    return False
                row.add(val)

                # Column check
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Square check
                idx = (r // 3) * 3 + (c // 3)
                if val in squares[idx]:
                    return False
                squares[idx].add(val)

        return True