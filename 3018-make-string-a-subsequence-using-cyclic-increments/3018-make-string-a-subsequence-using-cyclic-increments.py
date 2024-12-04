class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = len(str2)-1

        for k in range(len(str1)-1, -1, -1):
            if str1[k] == str2[i] or (ord(str1[k])+1)%97%26 == ord(str2[i])%97%26:
                i -= 1
            if i == -1:
                return True
        return False