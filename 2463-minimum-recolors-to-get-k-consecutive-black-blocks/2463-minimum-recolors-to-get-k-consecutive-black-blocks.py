class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count('W')
        res = len(blocks)
        for i in range(k, len(blocks)):
            res = min(res, white)
            if blocks[i] == 'W':
                white += 1
            if blocks[i-k] == 'W':
                white -= 1
            
        return min(res, white)