class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1]-position[0]
        
        def check(force):
            count = 0
            tmp = position[0]
            for i in range(len(position)):
                if position[i] - tmp >= force:
                    count += 1
                    tmp = position[i]
                if count == m-1:
                    return True
            return False

        while l <= r:
            mid = (l+r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r