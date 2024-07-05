class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        count = defaultdict(int)
        for i in range(len(tasks)):
            if tasks[i] in count and day - count[tasks[i]] <= space:
                day += (space - (day - count[tasks[i]]))
            day += 1
            count[tasks[i]] = day
        return day