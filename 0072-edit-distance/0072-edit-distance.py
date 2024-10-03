class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            if i == len(word1) and j == len(word2): return 0
            if i ==  len(word1) or j == len(word2): return abs(len(word1) - i - (len(word2)-j))

            insert = dfs(i, j+1) + 1
            delete = dfs(i+1, j) + 1
            replace = dfs(i+1, j+1) + (1 if word1[i] != word2[j] else 0)

            return min(insert, delete, replace)

        res = dfs(0, 0) 
        return res
        
