class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        N = len(s)
        dp = [[False]*N for _ in range(N)]            
        left, right = 0, 1
        for l in range(1, N+1):
            for i in range(N-l+1):
                j = i+l-1

                if i == j or (i+1 == j and s[i] == s[j]) or (s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j-i) > (left-right):
                        left = i
                        right = j
                        # res = s[i:j+1]

        return s[left:right+1]