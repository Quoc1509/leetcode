class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = 26*5*10**4
        pre = [0] * (len(s)+1)
        for i in range(len(shifts)):
            a,b,c = shifts[i]
            if c == 0:
                pre[a] += -1
                pre[b+1] += 1
            else:
                pre[a] += 1
                pre[b+1] += -1

        for i in range(1, len(pre)):
            pre[i] += pre[i-1]

        res = ''
        for i in range(len(pre)-1):
            convert = (ord(s[i])-97+pre[i]+N)%26
            res += chr(97+convert)
        return res
