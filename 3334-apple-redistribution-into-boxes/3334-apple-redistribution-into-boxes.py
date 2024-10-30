class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apples = sum(apple)
        total = 0
        for i in range(len(capacity)):
            total += capacity[i]
            if total >= apples:
                return i+1
        return -1
