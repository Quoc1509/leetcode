class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = defaultdict(int)
        def backTracking(total):
            if total == 0: return 0
            if total < 0: return inf
            if total in memo: return memo[total]
            count = inf
            for i in coins:
                temp = backTracking(total-i)
                count = min(count, temp)
            memo[total] = count + 1
            return memo[total]
        res = backTracking(amount)
        return res if res != inf else -1 