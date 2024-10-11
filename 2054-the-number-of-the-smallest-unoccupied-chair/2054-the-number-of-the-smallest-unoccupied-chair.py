class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort()

        freeChair = [i for i in range(len(times))]
        heap = []
        for a, b in times:
            while heap and heap[0][0] <= a:
                end, chair = heappop(heap)
                heappush(freeChair, chair)
            if a == target[0]:
                return freeChair[0]
            else:
                chair = heappop(freeChair)
                heappush(heap, (b, chair))
        return -1