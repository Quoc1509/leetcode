class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            if 0 in matrix[i]:
                for j in range(N):
                    if matrix[i][j] == 0:
                        continue
                    matrix[i][j] = -inf
                 
        for i in range(N):
            check = 0
            for j in range(M):   
                if matrix[j][i] == 0:
                    check = 1
                    break
            if check:
                for j in range(M):
                    if matrix[j][i] == 0:
                        continue
                    matrix[j][i] = -inf

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    continue
                if matrix[i][j] == -inf:
                    matrix[i][j] = 0
        