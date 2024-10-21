class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for a, b in intervals:
            temp = 0
            if heap and heap[0] <= a:
                temp = heappop(heap)
            heappush(heap, max(b, temp))
        # print(heap)
        return len(heap)