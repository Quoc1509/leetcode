class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * pow(cars, 2)
        def check(minutes):
            car = 0
            for i in ranks:
                car += floor(sqrt(minutes / i))
            return car
        while l <= r:
            m = (l+r)//2
            temp = check(m)
            if temp >= cars:
                r = m - 1 
            else:
                l = m + 1
        return l
