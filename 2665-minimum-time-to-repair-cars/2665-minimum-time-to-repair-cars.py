class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, max(ranks)*cars*cars

        def check(mid):
            count = 0
            for num in ranks:
                count += int(sqrt(mid/num))
                if count >= cars:
                    return True
            return False

        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
