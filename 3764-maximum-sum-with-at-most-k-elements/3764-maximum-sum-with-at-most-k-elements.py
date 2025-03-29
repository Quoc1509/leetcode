class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        res = []
        M, N = len(grid), len(grid[0])
        for i in range(M):
            heap = []
            for j in range(N):
                heappush(heap, grid[i][j])
                if len(heap) > limits[i]: 
                    heappop(heap)
            while heap:
                heappush(res, heappop(heap))
                if len(res) > k:
                    heappop(res)
        return sum(res)
                
            