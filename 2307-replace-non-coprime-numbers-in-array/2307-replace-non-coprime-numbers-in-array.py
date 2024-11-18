class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(num)
            while len(res) > 1 and gcd(res[-1], res[-2]) > 1:
                first = res.pop()
                second = res.pop()
                res.append(lcm(first, second))
        return res