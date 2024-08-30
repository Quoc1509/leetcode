class Solution:
    def totalNQueens(self, n: int) -> int:
        col = [True] * n
        dia1 = [True] * (2*n-1)
        dia2 = [True] * (2*n-1)
        count = [0]
        def backTracking(r):
            if r == n:
                count[0] += 1
                return
            for c in range(n):
                if col[c] and dia1[r+c] and dia2[r-c+n-1]:
                    col[c] = False
                    dia1[r+c] = False
                    dia2[r-c+n-1] = False

                    backTracking(r+1)
                    col[c] = True
                    dia1[r+c] = True
                    dia2[r-c+n-1] = True
        backTracking(0)
        return count[0]