class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # arr = [float('inf') for i in range(amount+1)]
        # arr[0] = 0
        
        # for coin in coins:
        #     for j in range(coin, amount + 1):
        #         arr[j] = min(arr[j], arr[j - coin] + 1)

        # if arr[amount] != float('inf'):
        #     return arr[amount]
        # else: return -1

        @cache
        def DP(total):
            if total == 0:
                return 0
            if total < 0:
                return inf
            res = inf
            for num in coins:
                res = min(res, DP(total-num))
            return res + 1
        res = DP(amount)
        return res if res != inf else -1
        
