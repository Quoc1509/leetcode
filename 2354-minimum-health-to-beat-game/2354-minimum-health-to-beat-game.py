class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        res = sum(damage)
        maxNum = max(damage)

        res -= maxNum
        if maxNum > armor:
            res += maxNum-armor
        return res+1