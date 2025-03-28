class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def DFS(i, money):
            if money == 0:
                return 1
            if money < 0 or i >= len(coins):
                return 0
            res = 0
            res += DFS(i+1, money) + DFS(i, money-coins[i])

            return res
        return DFS(0, amount)