class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = sorted([grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))])
        res = 0
        mid = len(arr) // 2
        for num in arr:
            if abs(num-arr[mid]) % x == 0:
                res += (abs(num-arr[mid]) // x)
            else:
                return -1
        return res