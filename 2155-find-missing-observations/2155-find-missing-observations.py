class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        N, s = len(rolls), sum(rolls)
        extra = (mean * (N+n)) - s
        if extra <= 0 or extra / 6 > n: return []
        res = [extra // n] * n
        if res[0] == 0: return []
        ss = sum(res)
        m = (ss + s) / (n+N)
        # print(m, ss, s, n)
        i = 0
        while m < mean:
            i = (i + 1) % len(res)
            res[i] += 1
            ss += 1
            m = (ss+s)/(n+N)
            
        return res if m == mean else []