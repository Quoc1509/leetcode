class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = [0] * n
        usedRoom = []
        freeRoom = [i for i in range(n)]
        meetings.sort()
        for start, end in meetings:
            while usedRoom and usedRoom[0][0] <= start:
                e, r = heappop(usedRoom)
                res[r] += 1
                heappush(freeRoom, r)

            if len(freeRoom) > 0:
                room = heappop(freeRoom)
                heappush(usedRoom, (end, room))
            else:
                e, r = heappop(usedRoom)
                res[r] += 1
                heappush(usedRoom, (end+(e-start), r))

        while usedRoom:
            e, r = heappop(usedRoom)
            res[r] += 1
        ans, maxUse = 0, 0
        for i, e in enumerate(res):
            if e > maxUse:
                maxUse = e
                ans = i
        return ans


