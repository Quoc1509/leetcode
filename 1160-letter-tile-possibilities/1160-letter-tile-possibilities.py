class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def BT(s, check):
            res.add(s)
            for i in range(len(tiles)):
                if (1<<i) & check:
                    continue
                BT(s+tiles[i], check|(1<<i))
            
        BT('', 0)
        return len(res)-1