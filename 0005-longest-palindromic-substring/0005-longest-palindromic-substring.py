class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        N = len(s)
        dp = [[False]*N for _ in range(N)]            

        for l in range(1, N+1):
            for i in range(N-l+1):
                j = i+l-1

                if i == j or (i+1 == j and s[i] == s[j]) or (s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j-i+1) > len(res):
                        res = s[i:j+1]

        return res