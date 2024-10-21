class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, visit):
            
            if i == len(s):
                return 0
            res = 0
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp not in visit:
                    visit.add(temp)
                    res = max(res, 1 + dfs(j+1, visit))
                    visit.remove(temp)
            return res
                    
        return dfs(0, set())
