class Solution:
    def minLength(self, s: str) -> int:
        res = []
        for i in s:
            # if not res:
            #     res.append(i)
            #     continue
            if res and ((i == 'B' and res[-1] == 'A') or (i == 'D' and res[-1] == 'C')):
                res.pop()
                continue
            res.append(i)
        return len(res)
