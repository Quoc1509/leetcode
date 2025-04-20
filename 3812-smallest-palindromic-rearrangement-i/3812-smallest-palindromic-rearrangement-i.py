class Solution:
    def smallestPalindrome(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            arr[ord(c)-ord("a")] += 1
        res = ""
        extra = ""
        for i in range(26):
            while arr[i] > 1:
                res += chr(i+97)
                arr[i] -= 2
            if arr[i] == 1:
                extra = chr(i+97)
        return res + extra + res[::-1]