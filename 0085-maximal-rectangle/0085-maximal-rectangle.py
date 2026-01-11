class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        res = 0
        A = [0] * (N+1)
        for i in range(M):
            stack = []
            for j in range(N):
                if matrix[i][j] == '1':
                    A[j] += 1
                else:
                    A[j] = 0
            print(A)
            for j in range(N+1):
                while stack and A[stack[-1]] >= A[j]:
                    w = stack.pop()
                    res = max(res, A[w] * (j-(stack[-1] if stack else -1)-1))
                stack.append(j)
        return res