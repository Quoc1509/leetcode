class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        def checkPalindrome(start, end):
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)):
            res += checkPalindrome(i, i)
            res += checkPalindrome(i, i+1)
        return res