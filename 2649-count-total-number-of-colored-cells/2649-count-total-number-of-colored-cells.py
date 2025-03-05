class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(n):
            res += (i*4)
        return res