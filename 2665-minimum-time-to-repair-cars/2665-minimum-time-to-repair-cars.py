class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        l, r = min(ranks), cars*cars*max(ranks)

        def check(mins):
            res = 0
            for i in ranks:
                res += floor(sqrt(mins / i))
            return res >= cars

        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l