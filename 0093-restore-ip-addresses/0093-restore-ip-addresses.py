class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        if N > 12: return []
        res = []

        def backTracking(ip, i):
            if i == N and len(ip) == 4:
                res.append('.'.join(ip))
                return
            if i < N:
                backTracking(ip+[s[i]], i+1)
            if i + 1 < N:
                temp = s[i:i+2]
                if temp[0] != '0':
                    backTracking(ip+[temp], i+2)
            if i + 2 < N:
                temp = s[i:i+3]
                if temp[0] != '0' and int(temp) < 256:
                    backTracking(ip+[temp], i + 3)
        
        backTracking([], 0)
        return res
                