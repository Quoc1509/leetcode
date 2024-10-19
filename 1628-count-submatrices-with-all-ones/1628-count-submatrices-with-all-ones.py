class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        for i in range(M):
            for j in range(N):
                if mat[i][j] and i > 0:
                    mat[i][j] += mat[i-1][j]
        def F(A):
            A.append(0)
            area = [0] * len(A)
            stack = []
            for i in range(len(A)):
                while stack and A[stack[-1]] > A[i]:
                    stack.pop()
                if stack:
                    area[i] = A[i] * (i - stack[-1]) + area[stack[-1]]
                else:
                    area[i] = A[i] * (i+1)
                stack.append(i)
            return sum(area)

        res = 0
        for i in range(M):
            res += F(mat[i])

        return res