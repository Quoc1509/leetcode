class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        s = ''
        for i in range(m):
            s += word1[i] + word2[i]
        s += word1[m:]
        s += word2[m:]
        return s