class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        M = len(grid[0])
        pre1 = [0] * (M+1)
        pre2 = [0] * (M+1)
        for i in range(M):
            pre1[i+1] = pre1[i]+grid[0][i]
            pre2[M-i-1] = pre2[M-i] + grid[1][M-i-1]
        maxNum = 0
        res = inf
        for i in range(1,len(pre1)):
            temp = max(pre1[-1]-pre1[i], pre2[0]-pre2[i-1])
            if temp <= pre1[i] + pre2[i-1]:
                res = min(res, temp)
        return res