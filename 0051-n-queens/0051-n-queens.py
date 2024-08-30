class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        dia1 = set()
        dia2 = set()
        res = []
        def backTracking(rows, r):
            if r == n:
                res.append(rows[:])            
                return
            row = ['.'] * n
            for c in range(n):
                if c not in col and (r+c) not in dia1 and (r-c+n-1) not in dia2:
                    col.add(c)
                    dia1.add(r+c)
                    dia2.add(r-c+n-1)

                    row[c] = 'Q'
                    temp = ''.join(row)                   
                    rows.append(temp)

                    backTracking(rows, r+1)

                    rows.pop()
                    row[c] = "."

                    col.remove(c)
                    dia1.remove(r+c)
                    dia2.remove(r-c+n-1)
        backTracking([], 0)
        return res
