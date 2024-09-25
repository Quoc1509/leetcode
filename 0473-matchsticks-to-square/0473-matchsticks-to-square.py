class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: return False
        slide = total // 4
        memo = {}
        # @cache
        def backTracking(length, count, visit):
            if count == 4: return True
            if length > slide: return False
            if (length, count, visit) in memo: return memo[(length, count, visit)]
            for i in range(len(matchsticks)):
                if (1<<i) & visit:
                    continue
                length += matchsticks[i]
                if length == slide:
                    if backTracking(0, count + 1, (1<<i)|visit):
                        memo[(length, count, visit)] = True
                        return memo[(length, count, visit)]
                else:
                    if backTracking(length, count, (1<<i)|visit):
                        memo[(length, count, visit)] = True
                        return memo[(length, count, visit)]
                length -= matchsticks[i]
            memo[(length, count, visit)] = False
            return memo[(length, count, visit)]
        
        return backTracking(0,0,0)


                