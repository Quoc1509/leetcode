class Solution:
    def compressedString(self, word: str) -> str:
        res = ''
        cur = 1
        for i in range(1, len(word)):
            if word[i-1] != word[i] or cur == 9:
                res += str(cur)+word[i-1]
                cur = 1
            else:
                cur += 1
        if cur > 0:
            res += str(cur) + word[-1]
        return res
