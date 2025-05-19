class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a >= b+c or b >= a+c or c >= a + b:
            return 'none'
        if a == b == c:
            return 'equilateral'
        elif a == b or a == c or b == c:
            return 'isosceles'
        else:
            return 'scalene'