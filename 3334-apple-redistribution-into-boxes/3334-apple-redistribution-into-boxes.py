class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        l, r = 1, len(capacity)-1
        apples = [sum(apple)]
        def check(m):
            total = sum(capacity[:m])
            return total >= apples[0]
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
