class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def check(i, s):
            count = 0
            for j in range(i, len(s)):
                count += ord(s[j])
            return count 

        @cache
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return 0
            if i1 == len(s1):
                return check(i2, s2)
            if i2 == len(s2):
                return check(i1, s1)
            if s1[i1] == s2[i2]:
                return dfs(i1+1, i2+1)

            one = dfs(i1+1, i2) + ord(s1[i1]) if s1[i1] != s2[i2] else 0
            two = dfs(i1, i2+1) + ord(s2[i2]) if s1[i1] != s2[i2] else 0
            return min(one, two)
            

        return dfs(0, 0)