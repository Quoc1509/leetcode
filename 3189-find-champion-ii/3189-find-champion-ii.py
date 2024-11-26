class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d = [0] * n
        for a, b in edges:
            d[b] += 1
        res = -1
        for i in range(n):
            if d[i] == 0:
                if res != -1:
                    return -1
                res = i
                
        return res