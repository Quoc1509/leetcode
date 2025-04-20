class Solution:
    def smallestPalindrome(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            arr[ord(c)-ord("a")] += 1
        first = ""
        second = "" 
        extra = -1
        for i in range(26):
            while arr[i] > 1:
                first += chr(i+97)
                second += chr(i+97)
                arr[i] -= 2
            if arr[i] == 1:
                extra = i
        return first + (chr(extra+97) if extra != -1 else "") + second[::-1]