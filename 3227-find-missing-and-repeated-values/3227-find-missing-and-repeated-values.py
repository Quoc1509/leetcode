class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        total = 0
        sumA = sum([i for i in range(1, N*N+1)])
        temp = set()
        res = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] in temp:
                    res.append(grid[i][j])
                else:
                    total += grid[i][j]
                    temp.add(grid[i][j])
        res.append(sumA-total)
        return res