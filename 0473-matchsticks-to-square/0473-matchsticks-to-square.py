class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: return False
        slide = total // 4
        @cache
        def backTracking(length, count, visit):
            if count == 4: return True
            if length > slide: return False
            for i in range(len(matchsticks)):
                if (1<<i) & visit:
                    continue
                length += matchsticks[i]
                if length == slide:
                    if backTracking(0, count + 1, (1<<i)|visit):
                        return True
                else:
                    if backTracking(length, count, (1<<i)|visit):
                        return True
                length -= matchsticks[i]
            return False
        
        return backTracking(0,0,0)


                