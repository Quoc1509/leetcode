class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = sorted(tiles)
        res = [0]  

        def backtrack(used):
            res[0] += 1 
            for i in range(len(s)):
                if (1 << i) & used: 
                    continue
                if i > 0 and s[i] == s[i - 1] and not ((1 << (i - 1)) & used):
                    continue 
                
                backtrack(used | (1 << i)) 
        
        backtrack(0)
        return res[0] - 1 
