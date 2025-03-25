class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        vertical = []
        horizontal = []
        for a,b,c,d in rectangles:
            vertical.append((a, c))
            horizontal.append((b, d))
        
        def check(arr):
            count = -1
            end = 0
            for s, e in arr:
                if s >= end:
                    count += 1
                    end = e
                else:
                    end = max(e, end)
                if count == 2:
                    return True
            return False
        
        if check(sorted(vertical)) or check(sorted(horizontal)):
            return True
        return False