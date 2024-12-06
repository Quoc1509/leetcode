class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        total = 0
        res = 0
        for i in range(1, n+1):
            if total + i > maxSum:
                break
            if i not in banned:
                total += i
                res += 1
        return res