class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: [x[0], x[1]])
        cur = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            start, end  = intervals[i]
            if start > cur[-1]:
                res.append(cur[:])
                cur = [start, end]
            else:
                cur[1] = max(end, cur[1])
        res.append(cur[:])
        return res