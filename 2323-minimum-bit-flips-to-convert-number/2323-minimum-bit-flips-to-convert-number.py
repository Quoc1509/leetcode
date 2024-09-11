class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 and goal > 0:
            s = start % 2
            start //= 2
            g = goal % 2
            goal //= 2
            if s != g:
                count += 1
        m = max(start, goal)
        while m > 0:
            if m%2 != 0:
                count += 1
            m //= 2
        return count
