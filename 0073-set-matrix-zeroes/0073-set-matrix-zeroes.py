class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        zeros = []
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        visitRow = set()
        visitCol = set()
        def setZero(ind, rc):
            if rc == 1 and ind not in visitRow:
                visitRow.add(ind)
                for c in range(N):
                    matrix[ind][c] = 0
            elif rc == 0 and ind not in visitCol:
                visitCol.add(ind)
                for r in range(M):
                    matrix[r][ind] = 0
        for r, c in zeros:
            setZero(r, 1)
            setZero(c, 0)