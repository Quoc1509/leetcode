from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        res = 0
        for i in range(1, len(heights)):
            temp = heights[i] - heights[i - 1]

            if temp > 0:
                heapq.heappush(heap, temp)
                
                # Use bricks for the smallest difference so far
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                
                # If we run out of bricks, return the current position
                if bricks < 0:
                    return res
            
            res += 1

        return res
