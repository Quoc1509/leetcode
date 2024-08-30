class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [True] * n
        dia1 = [True] * (2*n-1)
        dia2 = [True] * (2*n-1)
        res = []
        def backTracking(rows, r):
            if r == n:
                res.append(rows[:])            
                return
            row = ['.'] * n
            for c in range(n):
                if col[c] and dia1[r+c] and dia2[r-c+n-1]:
                    col[c] = False
                    dia1[r+c] = False
                    dia2[r-c+n-1] = False

                    row[c] = 'Q'
                    temp = ''.join(row)                   
                    rows.append(temp)

                    backTracking(rows, r+1)

                    rows.pop()
                    row[c] = "."

                    col[c] = True
                    dia1[r+c] = True
                    dia2[r-c+n-1] = True
        backTracking([], 0)
        return res
