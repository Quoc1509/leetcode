
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = math.lcm(a,b)
        bc = math.lcm(b,c)
        ac = math.lcm(a,c)
        abc = math.lcm(a,b,c)
        l, r = 1, 2*(10**9)

        def check(m):
            total = (m//a) + (m//b) + (m//c)
            res = total - (m//ab) - (m//bc) - (m//ac) + (m//abc)
            return res >= n

        while l <= r:
            mid = (l+r)//2

            if check(mid):
                r = mid-1
            else:
                l = mid+1
        return l