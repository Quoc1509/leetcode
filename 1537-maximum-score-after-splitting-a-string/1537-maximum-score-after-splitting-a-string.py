class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')
        # if one == len(s) or one == 0:
        #     return len(s)-1
        zero = 0
        res = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero += 1
            elif s[i] == '1':
                one -= 1
            res = max(res, one+zero)
        return res