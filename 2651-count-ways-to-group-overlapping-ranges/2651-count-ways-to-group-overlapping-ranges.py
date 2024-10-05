class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        maxEnd = -inf
        count = 0
        for i in range(len(ranges)):
            if maxEnd < ranges[i][0]:
                count += 1
            maxEnd = max(maxEnd, ranges[i][1])
        return pow(2, count, 10**9+7)