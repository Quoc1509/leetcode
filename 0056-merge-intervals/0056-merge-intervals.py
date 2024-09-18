class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            a, b= intervals[i]
            if a > end:
                res.append([start, end])
                start, end = a, b
            else:
                end = max(end, b)
        res.append([start, end])
        return res