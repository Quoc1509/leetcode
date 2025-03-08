class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        res = len(blocks)
        for i in range(len(blocks)):   
            if i >= k:
                res = min(res, white)  
                if blocks[i-k] == 'W':
                    white -= 1       
            if blocks[i] == 'W':
                white += 1            
        return min(res, white)