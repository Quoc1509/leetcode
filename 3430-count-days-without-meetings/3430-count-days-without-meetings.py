class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        endTime = meetings[0][1]
        res = meetings[0][0]-1
        for start, end in meetings:
            res += max(start-endTime-1, 0)
            endTime = max(endTime, end)
        return res+max(days-endTime, 0)