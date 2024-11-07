class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(33):
            count = 0
            for num in candidates:
                if (1 << i)&num:
                    count += 1
            res = max(res, count)
        return res

