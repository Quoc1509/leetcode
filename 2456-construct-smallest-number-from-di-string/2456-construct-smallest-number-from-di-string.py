class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = [inf]
        def BT(i, val, check):
            if i > len(pattern):
                res[0] = min(res[0], val)
                return
            
            for j in range(1, 10):
                if val == 0:
                    BT(1, j, (1<<j)|check)
                if (1<<j)&check:
                    continue
                
                if pattern[i-1] == 'I':
                    if j > val % 10:
                        BT(i+1, val*10+j, check|(1<<j))
                else:
                    if j < val % 10:
                        BT(i+1, val*10+j, check|(1<<j))
        
        BT(0, 0, 0)
        return str(res[0])
