class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = sorted(tiles)
        res = [0]  

        def backtrack(used):
            res[0] += 1 
            i = 0
            while i < len(s):
                if (1 << i) & used: 
                    i += 1
                    continue
                backtrack(used|(1<<i)) 
                j = i+1
                while j < len(s) and s[i] == s[j]:
                    j += 1
                i = j
               
        
        backtrack(0)
        return res[0] - 1 
