class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        l, res, total = 0, 0, 0
        maxTime = deque()
        for r in range(len(chargeTimes)):
            total += runningCosts[r]
            while maxTime and chargeTimes[r] > maxTime[-1]:
                maxTime.pop()
            maxTime.append(chargeTimes[r])
            # print(r, maxTime)
            while maxTime and  maxTime[0] + (r-l+1) * total > budget:
                total -= runningCosts[l]
                if chargeTimes[l] == maxTime[0]:
                    maxTime.popleft()
                l += 1
            res = max(res, r-l+1)
        return res