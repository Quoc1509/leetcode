class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = [inf]
        def BT(i, val, check):
            if i > len(pattern):
                res[0] = val
                return True
            
            for j in range(1, 10):
                if val == 0:
                    if BT(1, j, (1<<j)|check):
                        return True
                if (1<<j)&check:
                    continue
                
                if (pattern[i-1] == 'I' and j > val % 10) or (pattern[i-1] == 'D' and j < val % 10):
                        if BT(i+1, val*10+j, check|(1<<j)):
                            return True
        
        BT(0, 0, 0)
        return str(res[0])
