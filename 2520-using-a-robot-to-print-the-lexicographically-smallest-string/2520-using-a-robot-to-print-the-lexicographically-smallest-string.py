class Solution:
    def robotWithString(self, s: str) -> str:
        temp = [i for i in range(len(s))]
        for i in range(len(s)-2, -1, -1):
            if s[temp[i+1]] < s[temp[i]]:
                temp[i] = temp[i+1]
        stk = []
        res = ''
        for i in range(len(s)):
            while stk and stk[-1] <= s[temp[i]]:
                res += stk.pop()
            stk.append(s[i])
            
        while stk:
            res += stk.pop()
        return res