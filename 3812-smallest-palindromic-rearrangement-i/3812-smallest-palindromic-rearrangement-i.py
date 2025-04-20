class Solution:
    def smallestPalindrome(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            arr[ord(c)-ord("a")] += 1
        first = ""
        second = "" 
        extra = ""
        for i in range(26):
            while arr[i] > 1:
                first += chr(i+97)
                second += chr(i+97)
                arr[i] -= 2
            if arr[i] == 1:
                extra = chr(i+97)
        return first + extra + second[::-1]