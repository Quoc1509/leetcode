class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[1])
        res = events[0][2]
        # print(events)
        def check(i):
            l, r = 0, i
            while l <= r:
                m = (l+r)//2
                if events[m][1] >= events[i][0]:
                    r = m - 1
                else:
                    l = m + 1
            return l
        for i in range(1, len(events)):
            index = check(i)
            if index == 0:
                res = max(res, events[i][2])
            else:
                res= max(res, events[i][2]+events[index-1][2])
            events[i][2] = max(events[i][2], events[i-1][2])
        # print(res)
        return res
