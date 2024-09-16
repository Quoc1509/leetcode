class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        memo = {}
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1, i2) in memo: return memo[(i1,i2)]
            
            res1 = dfs(i1+1, i2) if i1 < len(s1) and s3[i1+i2] == s1[i1] else False

            res2 = dfs(i1, i2+1) if i2 < len(s2) and s3[i1+i2] == s2[i2] else False
            
            memo[(i1, i2)] = res1 or res2
            return memo[(i1, i2)]
        return dfs(0, 0)
            