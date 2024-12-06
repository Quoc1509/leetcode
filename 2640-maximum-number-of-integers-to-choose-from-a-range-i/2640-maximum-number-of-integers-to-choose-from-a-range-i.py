class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        total = 0
        res = set()
        for i in range(1, n+1):
            if i not in banned:
                total += i
                res.add(i)
        # print(res)
        for i in range(n, 0, -1):
            if total > maxSum and i in res:
                total -= i
                res.remove(i)
        # print(res)
        return len(res)