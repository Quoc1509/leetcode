class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * (len(s)+1)
        for i in range(len(shifts)):
            a,b,c = shifts[i]
            if c == 0:
                pre[a] += -1
                pre[b+1] += 1
            else:
                pre[a] += 1
                pre[b+1] += -1
        
        convert = (ord(s[0])-97+pre[0])%26
        res = chr(97+convert)
        for i in range(1, len(pre)-1):
            pre[i] += pre[i-1]
            convert = (ord(s[i])-97+pre[i])%26
            res += chr(97+convert)
        # res = ''
        # for i in range(len(pre)-1):
        #     convert = (ord(s[i])-97+pre[i])%26
        #     res += 
        return res
