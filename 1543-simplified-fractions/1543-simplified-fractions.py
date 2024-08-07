class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        visited = set()
        for i in range(2, n+1):
            for j in range(1, i):
                if (j/i) not in visited:
                    res.append(str(j) + '/' + str(i))
                    visited.add((j/i))
        return res