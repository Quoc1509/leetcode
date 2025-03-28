class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # heap = []
        # for a, b in intervals:
        #     temp = 0
        #     if heap and heap[0] <= a:
        #         temp = heappop(heap)
        #     heappush(heap, max(b, temp))
        # return len(heap)

        maxEnd = 0
        for a, b in intervals:
            maxEnd = max(b, maxEnd)
        room = [0] * (maxEnd+1)
        for a, b in intervals:
            room[a] += 1
            room[b] -= 1
        res = 0
        for i in range(maxEnd):
            room[i+1] += room[i]
            res = max(res, room[i+1])
        return res