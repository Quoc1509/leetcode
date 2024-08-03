class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count1 = Counter(target)
        count2 = Counter(arr)
        return count1 == count2