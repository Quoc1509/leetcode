class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = ["L"] + list(dominoes) + ["R"]
        i = 0
        def update(s, e, c):
            for i in range(s, e):
                res[i] = c
        while i < len(res)-1:
            j = i + 1
            while j < len(res)-1 and res[j] == '.':
                j += 1
            if res[i] == res[j]:
                update(i, j, res[i])
            elif res[i] == 'R' and res[j] == 'L':
                l, r = i, j
                while l < r:
                    res[l] = 'R'
                    res[r] = 'L'
                    l += 1
                    r -= 1
            i = j
        ans = ""
        for i in range(1, len(res)-1):
            ans += res[i]      
        return ans    