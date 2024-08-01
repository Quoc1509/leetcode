class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        alpha = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            alpha[i][i] = 0

        for i in range(len(cost)):
            a = ord(original[i]) - 97
            b = ord(changed[i]) - 97
            
            alpha[a][b] = min(cost[i], alpha[a][b])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    alpha[i][j] = min(alpha[i][j], alpha[i][k]+alpha[k][j])
        res = 0
        for i in range(len(source)):
            a = ord(source[i]) - 97
            b = ord(target[i]) - 97
            if alpha[a][b] == inf: return -1

            res += alpha[a][b]

        return res