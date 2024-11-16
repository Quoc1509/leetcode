class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for num in nums:

            for prime in range(2, int(sqrt(num))+1):
                while num % prime == 0:
                    num //= prime
                    res.add(prime)
            if num > 1:
                res.add(num)
        return len(res)