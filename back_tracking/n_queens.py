from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []

        cols = set()       # columns with queens
        posDiag = set()    # r + c (↘ diagonal)
        negDiag = set()    # r - c (↙ diagonal)

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue  # skip invalid spot

                # place queen
                board[r][c] = 'Q'
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                dfs(r + 1)

                # backtrack
                board[r][c] = '.'
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        dfs(0)
        return res

print(Solution().solveNQueens(4))
# Output:
# [
#  [".Q..","...Q","Q...","..Q."],
#  ["..Q.","Q...","...Q",".Q.."]
# ]
