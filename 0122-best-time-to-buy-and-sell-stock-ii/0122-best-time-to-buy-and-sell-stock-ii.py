class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mStock = prices[0]
        for i in prices:
            if i < mStock:
                mStock = i
                continue
            res += (i-mStock)
            mStock = i
        return res