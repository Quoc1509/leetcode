class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        table = [0] * (len(s)+1)
        plate = []
        for i in range(len(s)):
            if s[i] == '*':
                table[i+1] = table[i] + 1
            else:
                plate.append(i)
                table[i+1] = table[i]
        plate.append(len(s))
        res = []
        for a, b in queries:
            
            l = bisect_left(plate, a)
            r = bisect_right(plate, b)-1
            if l >= r:
                res.append(0)
            else:
                res.append(table[plate[r]+1]-table[plate[l]])
        return res