class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for i in s:
            if len(res) >= 2 and res[-1] == res[-2] == i:
                continue
            res.append(i)
        return ''.join(res)