class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sr = ''
        for i in s:
            if i == '-':
                continue
            if i.isalpha():
                sr += i.upper()
            else:
                sr += i
        res = ''
        if len(sr) <= k: return sr
        r = len(sr)
        for l in range(len(sr)-k, -1, -k):
            if len(res) == 0:
                res += sr[l:r]
            else:
                res = sr[l:r] + '-' + res
            r = l

        if r > 0:
            res = sr[:r] + '-' + res
        return res
