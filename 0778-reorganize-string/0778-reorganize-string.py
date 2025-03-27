class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxF, maxC = 0, ''
        for ch, fre in count.items():
            if fre > maxF:
                maxF = fre
                maxC = ch
        if maxF > (len(s)+1)//2:
            return ''
        res = [''] * len(s)
        index = 0
        while count[maxC] > 0:
            res[index] = maxC
            count[maxC] -= 1
            index += 2
        
        for ch, freq in count.items():
            while freq > 0:
                if index >= len(s):
                    index = 1
                res[index] = ch
                index += 2
                freq -= 1
        return ''.join(res)