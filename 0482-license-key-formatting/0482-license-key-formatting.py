class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sr = ''
        for i in range(len(s)):
            if s[i].isalpha():
                sr += s[i].upper()
            else:
                sr += s[i]
        res = []

        temp = sr.split('-')
        
        cur = ''
        while temp:
            st = temp.pop()
            if len(cur) + len(st) == k:
                res.append(st+cur)
                cur = ''
            elif len(cur) + len(st) < k:
                cur = st + cur
            else:
                extra = len(cur) + len(st) - k
                cur = st[extra:] + cur
                res.append(cur)
                cur = ''
                temp.append(st[:extra])
        if cur:
            res.append(cur)
        
        return '-'.join(reversed(res))